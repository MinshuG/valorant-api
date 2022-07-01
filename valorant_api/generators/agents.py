import atexit
from http.client import HTTPException
from io import BytesIO
from typing import TYPE_CHECKING

import aiohttp
import asyncio
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from .utils import Rect, gradient_color, hex2rgb, vert_gradient

if TYPE_CHECKING:
    from ..agents import Agent


class AgentImageGenerator:  # total mess
    font_file: str
    resolution: tuple = (1024, 2048)
    ability_font_size: int = 25
    display_name_font_size: int = 100

    def __init__(self, font_file, session=None) -> None:
        self.font_file = font_file
        if session is None:
            self.session = aiohttp.ClientSession()
            atexit.register(self.close)
        else:
            self.session = session
        self._blank_image: Image.Image = Image.new("RGBA", self.resolution, (34, 30, 40))  # (240, 91, 87)
        atexit.register(self.close)

    def close(self):
        asyncio.run(self.session.close())

    async def generate(self, data: 'Agent') -> Image.Image:
        image = self._blank_image.copy()
        if data.background_gradient_colors not in (None, []):
            grad_image = ImageDraw.Draw(image)
            region = Rect(0, 0, *self.resolution)
            vert_gradient(grad_image, region, gradient_color, tuple(hex2rgb(col) for col in data.background_gradient_colors))

        if data.background is not None:
            bg_image = await self.image_downloader(data.background)            
            ratio = (self.resolution[1] / bg_image.size[0]) * 0.7
            bg_image = bg_image.resize((int(bg_image.size[0]*ratio), int(bg_image.size[1]*ratio)), Image.Resampling.LANCZOS)
            image.alpha_composite(bg_image, ((self.resolution[0]-bg_image.size[0])//2, (self.resolution[1]-bg_image.size[1])//2))

        if data.full_portraitV2 is not None:
            portrait = await self.image_downloader(data.full_portraitV2)
            ratio = (self.resolution[1] / portrait.size[0]) * 0.95
            portrait = portrait.resize((int(portrait.size[0]*ratio), int(portrait.size[1]*ratio)), Image.Resampling.LANCZOS)
        else:
            portrait = image.copy()

        # agent image
        offset = (int((image.size[0] - portrait.size[0]) / 2 + 100), int((image.size[1] - portrait.size[1]) / 2)) # center
        image.alpha_composite(portrait, offset)

        # blur
        crop_amt = self.resolution[1] - 184  # abilities offset from top
        blurred = image.copy().crop((0, crop_amt, self.resolution[0], self.resolution[1])).filter(ImageFilter.GaussianBlur(1))
        image.paste(blurred, (0, crop_amt))

        image = self.draw_name(image, data.display_name)

        num_abilities = len([x for x in data.abilities if x.slot != "Passive"])
        icon_offset = -(self.resolution[0] // (num_abilities+1))  # start offset from left
        for ability in data.abilities:
            if ability.slot == "Passive":
                continue
            if ability.display_icon is not None:
                icon = await self.image_downloader(ability.display_icon)
                icon = icon.resize((128, 128))
            else:
                icon = Image.new("RGBA", (128, 128))
            icon_offset += self.resolution[0] // (num_abilities)
            pos = (icon_offset, crop_amt + 10)  # crop_amt + ?? is offset from top
            image.alpha_composite(icon, pos)
            image = self.draw_ability_name(image, ability.display_name, pos)

        return image

    def draw_ability_name(self, image: Image.Image, text: str, position: tuple):
        if text is None:
            return image
        draw = ImageDraw.Draw(image)

        wraped = textwrap.wrap(text=text,width=20)

        font = ImageFont.truetype(self.font_file, min(self.ability_font_size,int((self.ability_font_size/len(wraped))/.7)))
        align = "center"
        x1, y1, x2, y2 = [position[0]-25, position[1]+160, position[0]+150, position[1]+120]
        w, h = draw.textsize(wraped[0], font=font)
        x = (x2 - x1 - w) / 2 + x1
        y = (y2 - y1 - h) / 2 + y1
        # draw.rectangle([x1, y1, x2, y2])  # bounding box

        draw.text((x, y), "\n".join(wraped), font=font, fill=(255, 255, 255, 255), align=align)
        return image

    def draw_name(self, image: Image.Image, text: str):
        image2 = Image.new("RGBA", (self.resolution[0], 512))
        draw = ImageDraw.Draw(image2)
        font = ImageFont.truetype(self.font_file, self.display_name_font_size)
        align = "left"
        x1, y1, x2, y2 = [0, 10, self.resolution[0], 125]
        w, h = draw.textsize(text, font=font)
        x = (x2 - x1 - w) / 2 + x1
        y = (y2 - y1 - h) / 2 + y1
        # draw.rectangle([x1, y1, x2, y2])  # bounding box
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 255), align=align)
        image2 = image2.rotate(90, expand=1)

        image.alpha_composite(image2, (0, 0))
        return image

    async def image_downloader(self, url: str) -> Image.Image:
        async with self.session.get(url) as response:
            if response.status == 200:
                image_bytes = BytesIO(await response.content.read())
                return Image.open(image_bytes).convert("RGBA")
            else:
                raise HTTPException(
                    f'An error occurred while downloading a image, status code {response.status}')

if __name__ == "__main__":
    import sys
    sys.path.append("L:\Coding Stuff\Valorant-api")
    import asyncio
    from valorant_api import AsyncValorantApi, SyncValorantApi
    import time

    async def generator_test():
        api = AsyncValorantApi(language = "fr-FR")
        agents = await api.get_agents()
        generator = AgentImageGenerator(r"valorant_api/fonts/Valorant Font.ttf")
        tasks = []
        for agent in agents:
            await generate(generator, agent)
        #     tasks.append(asyncio.create_task(generate(generator, agent)))
        # await asyncio.gather(*tasks)

    async def generate(generator, agent: 'Agent'):
        image = await generator.generate(agent)
        image.save(f"images/{agent.display_name.replace('/', '_')}_{agent.uuid}.png", "PNG") # KAY/O

    st = time.time()
    asyncio.get_event_loop().run_until_complete(generator_test())
    print("[Async: Generator] Took", time.time() - st)
