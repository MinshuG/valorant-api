import time

from valorant_api import SyncValorantApi, AsyncValorantApi
from valorant_api import generators
import asyncio

language = "en-US"


def synctest():
    api = SyncValorantApi(language=language)
    agents = api.get_agents()
    agent = api.search_agents_by_uuid("5f8d3a7f-467b-97f3-062c-13acf203c006")
    buddies = api.get_buddies()
    buddy = api.search_buddies_by_uuid("d6f5e6a4-4d42-b56d-03c3-92955d294f54")
    bundles = api.get_bundles()
    bundle = api.search_bundles_by_uuid("0dee7ef6-d3ea-400a-b15c-5b9524243439")
    content_tiers = api.get_contenttiers()
    content_tier = api.search_contenttier_by_uuid("0cebb8be-46d7-c12a-d306-e9907bfc5a25")
    currencies = api.get_currencies()
    currency = api.search_currencies_by_uuid("85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741")
    gamemodes = api.get_gamemodes()
    gamemode = api.search_gamemodes_by_uuid("96bd3920-4f36-d026-2b28-c683eb0bcac5")
    equippables = api.get_gamemode_equippables()
    equippable = api.search_gamemode_equippables_by_uuid("3de32920-4a8f-0499-7740-648a5bf95470")
    maps = api.get_maps()
    map = api.search_maps_by_uuid("7eaecc1b-4337-bbf6-6ab9-04b8f06b3319")
    playercards = api.get_playercards()
    playercard = api.search_playercards_by_uuid("33c1f011-4eca-068c-9751-f68c788b2eee")
    playertitles = api.get_playertitles()
    playertitle = api.search_playertitles_by_uuid("a65074fd-4937-734e-20fe-3cafa842c631")
    seasons = api.get_seasons()
    season = api.search_seasons_by_uuid("0df5adb9-4dcb-6899-1306-3e9860661dd3")
    themes = api.get_themes()
    theme = api.search_themes_by_uuid("38f408dc-416e-eda9-3ac5-21892c5f5ad1")
    weapons = api.get_weapons()
    weapon = api.search_weapons_by_uuid("63e6c2b6-4a8e-869c-3d4c-e38355226584")
    sprays = api.get_sprays()
    spray = api.search_sprays_by_uuid("3d2bcfc5-442b-812e-3c08-9180d6b36077")
    version = api.get_version()


async def Asynctest():
    api = AsyncValorantApi(language=language)
    agents = await api.get_agents()
    agent = await api.search_agents_by_uuid("5f8d3a7f-467b-97f3-062c-13acf203c006")
    buddies = await api.get_buddies()
    buddy = await api.search_buddies_by_uuid("d6f5e6a4-4d42-b56d-03c3-92955d294f54")
    bundles = await api.get_bundles()
    bundle = await api.search_bundles_by_uuid("0dee7ef6-d3ea-400a-b15c-5b9524243439")
    content_tiers = await api.get_contenttiers()
    content_tier = await api.search_contenttier_by_uuid("0cebb8be-46d7-c12a-d306-e9907bfc5a25")
    currencies = await api.get_currencies()
    currency = await api.search_currencies_by_uuid("85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741")
    gamemodes = await api.get_gamemodes()
    gamemode = await api.search_gamemodes_by_uuid("96bd3920-4f36-d026-2b28-c683eb0bcac5")
    equippables = await api.get_gamemode_equippables()
    equippable = await api.search_gamemode_equippables_by_uuid("3de32920-4a8f-0499-7740-648a5bf95470")
    maps = await api.get_maps()
    map = await api.search_maps_by_uuid("7eaecc1b-4337-bbf6-6ab9-04b8f06b3319")
    playercards = await api.get_playercards()
    playercard = await api.search_playercards_by_uuid("33c1f011-4eca-068c-9751-f68c788b2eee")
    playertitles = await api.get_playertitles()
    playertitle = await api.search_playertitles_by_uuid("a65074fd-4937-734e-20fe-3cafa842c631")
    seasons = await api.get_seasons()
    season = await api.search_seasons_by_uuid("0df5adb9-4dcb-6899-1306-3e9860661dd3")
    themes = await api.get_themes()
    theme = await api.search_themes_by_uuid("38f408dc-416e-eda9-3ac5-21892c5f5ad1")
    weapons = await api.get_weapons()
    weapon = await api.search_weapons_by_uuid("63e6c2b6-4a8e-869c-3d4c-e38355226584")
    sprays = await api.get_sprays()
    spray = await api.search_sprays_by_uuid("3d2bcfc5-442b-812e-3c08-9180d6b36077")
    version = await api.get_version()


async def generator_test():
    api = AsyncValorantApi(language=language)
    agents = await api.get_agents()
    generator = generators.AgentImageGenerator(r"valorant_api\fonts\Valorant Font.ttf")
    for agent in agents:
        image = await generator.generate(agent)
        image.save(f"images/{agent.uuid}.png", "PNG")


if __name__ == "__main__":
    st = time.time()
    synctest()
    print("[Sync] Took", time.time() - st)

    st = time.time()
    asyncio.get_event_loop().run_until_complete(Asynctest())
    print("[Async] Took", time.time() - st)

    st = time.time()
    asyncio.get_event_loop().run_until_complete(generator_test())
    print("[Async: Generator] Took", time.time() - st)
