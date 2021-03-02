import atexit
from io import BytesIO

import aiohttp
import asyncio
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from valorant_api.agents import Agent


class AgentImageGenerator:  # total mess
    font_file: str
    resolution: tuple = (1024, 1024)
    _blank_image: Image.Image = Image.new("RGBA", resolution, (240, 91, 87))
    ability_font_size: int = 25
    display_name_font_size: int = 100

    def __init__(self, font_file) -> None:
        self.font_file = font_file
        self.session = aiohttp.ClientSession()
        atexit.register(self.close)

    def close(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.session.close())

    async def generate(self, data: Agent) -> Image.Image:
        image = self._blank_image.copy()
        if data.bust_portrait is not None:
            portrait = await self.image_downloader(data.bust_portrait)
        else:
            portrait = image.copy()

        offset = (int((image.size[0] - portrait.size[0]) / 2 + 100), int((image.size[1] - portrait.size[1]) / 2))
        image.alpha_composite(portrait, offset)

        crop_amt = 850
        blurred = image.copy().crop((0, crop_amt, portrait.size[0], portrait.size[1])).filter(ImageFilter.GaussianBlur(20))

        image.paste(blurred, (0, crop_amt))
        image = self.draw_name(image, data.display_name)

        icon_offset = 50
        num_abilities = len([x for x in data.abilities if x.slot != "Passive"])
        for ability in data.abilities:
            if ability.slot == "Passive":
                continue
            if ability.display_icon is not None:
                icon = await self.image_downloader(ability.display_icon)
                icon = icon.resize((128, 128))
            else:
                icon = Image.new("RGBA", (128, 128))

            pos = (icon_offset, crop_amt + 10)
            image.alpha_composite(icon, pos)
            image = self.draw_ability_name(image, ability.display_name, pos)
            icon_offset += round(1024 / num_abilities)

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
        image2 = Image.new("RGBA", (1024, 512))
        draw = ImageDraw.Draw(image2)
        font = ImageFont.truetype(self.font_file, self.display_name_font_size)
        align = "left"
        x1, y1, x2, y2 = [400, 10, 900, 125]
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
                raise Exception(
                    f'An error occurred while downloading a image, status code {response.status}')
