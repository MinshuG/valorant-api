from .ceremonies import Ceremony
from .gear import Gear
from .events import Event
from .contracts import Contract
from .competitive import Competitive
from .competitivetiers import CompetitiveTier
from .sprays import Spray
from .sprays import Level as SprayLevel
from .agents import Agent
from .base_list import BaseList
from .buddies import Buddy
from .buddies import Level as BuddyLevel
from .bundles import Bundle
from .contenttiers import ContentTier
from .currencies import Currency
from .endpoints import Endpoints
from .gamemodes import GameMode, Equippable
from .maps import Map
from .playercards import PlayerCard
from .playertitles import PlayerTitle
from .seasons import Season
from .themes import Theme
from .version import Version
from .weapons import Chroma, Skin, Weapon, Level
from .levelborders import LevelBorder

from .httpclient import AsyncClient, SyncClient


class SyncValorantApi:
    """
Synchronous valorant-api wrapper
    """

    headers: dict
    client: SyncClient
    params: dict = {}

    def __init__(self, headers=None, language: str = "en-US"):
        if headers is None:
            headers = {}
        self.params["language"] = language
        self.headers = headers
        self.client = SyncClient(headers, params=self.params)

    def get_agents(self, *args, **kwargs) -> BaseList[Agent]:
        data = self.client.get(Endpoints.Agents, *args, **kwargs)
        return BaseList([Agent(x) for x in data])

    def search_agents_by_uuid(self, uuid: str, *args, **kwargs) -> Agent:
        data = self.client.get(f"{Endpoints.Agents}/{uuid}", *args, **kwargs)
        return Agent(data)

    def get_buddies(self, *args, **kwargs) -> BaseList[Buddy]:
        data = self.client.get(Endpoints.Buddies, *args, **kwargs)
        return BaseList([Buddy(x) for x in data])

    def search_buddies_by_uuid(self, uuid: str, *args, **kwargs) -> Buddy:
        data = self.client.get(f"{Endpoints.Buddies}/{uuid}", *args, **kwargs)
        return Buddy(data)

    def get_bundles(self, *args, **kwargs) -> BaseList[Bundle]:
        data = self.client.get(Endpoints.Bundles, *args, **kwargs)
        return BaseList([Bundle(x) for x in data])

    def search_bundles_by_uuid(self, uuid: str, *args, **kwargs) -> Bundle:
        data = self.client.get(f"{Endpoints.Bundles}/{uuid}", *args, **kwargs)
        return Bundle(data)

    def get_contenttiers(self, *args, **kwargs) -> BaseList[ContentTier]:
        data = self.client.get(Endpoints.ContentTiers, *args, **kwargs)
        return BaseList([ContentTier(x) for x in data])

    def search_contenttier_by_uuid(self, uuid: str, *args, **kwargs) -> ContentTier:
        data = self.client.get(f"{Endpoints.ContentTiers}/{uuid}", *args, **kwargs)
        return ContentTier(data)

    def get_currencies(self, *args, **kwargs) -> BaseList[Currency]:
        data = self.client.get(Endpoints.Currencies, *args, **kwargs)
        return BaseList([Currency(x) for x in data])

    def search_currencies_by_uuid(self, uuid: str, *args, **kwargs) -> ContentTier:
        data = self.client.get(f"{Endpoints.Currencies}/{uuid}", *args, **kwargs)
        return ContentTier(data)

    def get_ceremonies(self, *args, **kwargs) -> BaseList[Ceremony]:
        data = self.client.get(Endpoints.Ceremonies, *args, **kwargs)
        return BaseList([Ceremony(x) for x in data])

    def search_ceremonies_by_uuid(self, uuid: str, *args, **kwargs) -> Ceremony:
        data = self.client.get(f"{Endpoints.Ceremonies}/{uuid}", *args, **kwargs)
        return Ceremony(data)

    def get_gamemodes(self, *args, **kwargs) -> BaseList[GameMode]:
        data = self.client.get(Endpoints.GameMode, *args, **kwargs)
        return BaseList([GameMode(x) for x in data])

    def search_gamemodes_by_uuid(self, uuid: str, *args, **kwargs) -> GameMode:
        data = self.client.get(f"{Endpoints.GameMode}/{uuid}", *args, **kwargs)
        return GameMode(data)

    def get_gamemode_equippables(self, *args, **kwargs) -> BaseList[Equippable]:
        data = self.client.get(Endpoints.GamemodeEquippables, *args, **kwargs)
        return BaseList([Equippable(x) for x in data])

    def search_gamemode_equippables_by_uuid(self, uuid: str, *args, **kwargs) -> Equippable:
        data = self.client.get(f"{Endpoints.GamemodeEquippables}/{uuid}", *args, **kwargs)
        return Equippable(data)

    def get_maps(self, *args, **kwargs) -> BaseList[Map]:
        data = self.client.get(Endpoints.Maps, *args, **kwargs)
        return BaseList([Map(x) for x in data])

    def search_maps_by_uuid(self, uuid: str, *args, **kwargs) -> Map:
        data = self.client.get(f"{Endpoints.Maps}/{uuid}", *args, **kwargs)
        return Map(data)

    def get_playercards(self, *args, **kwargs) -> BaseList[PlayerCard]:
        data = self.client.get(Endpoints.PlayerCards, *args, **kwargs)
        return BaseList([PlayerCard(x) for x in data])

    def search_playercards_by_uuid(self, uuid: str, *args, **kwargs) -> PlayerCard:
        data = self.client.get(f"{Endpoints.PlayerCards}/{uuid}", *args, **kwargs)
        return PlayerCard(data)

    def get_playertitles(self, *args, **kwargs) -> BaseList[PlayerTitle]:
        data = self.client.get(Endpoints.PlayerTitles, *args, **kwargs)
        return BaseList([PlayerTitle(x) for x in data])

    def search_playertitles_by_uuid(self, uuid: str, *args, **kwargs) -> PlayerTitle:
        data = self.client.get(f"{Endpoints.PlayerTitles}/{uuid}", *args, **kwargs)
        return PlayerTitle(data)

    def get_seasons(self, *args, **kwargs) -> BaseList[Season]:
        data = self.client.get(Endpoints.Seasons, *args, **kwargs)
        return BaseList([Season(x) for x in data])

    def search_seasons_by_uuid(self, uuid: str, *args, **kwargs) -> Season:
        data = self.client.get(f"{Endpoints.Seasons}/{uuid}", *args, **kwargs)
        return Season(data)

    def get_themes(self, *args, **kwargs) -> BaseList[Theme]:
        data = self.client.get(Endpoints.Themes, *args, **kwargs)
        return BaseList([Theme(x) for x in data])

    def search_themes_by_uuid(self, uuid: str, *args, **kwargs) -> Theme:
        data = self.client.get(f"{Endpoints.Themes}/{uuid}", *args, **kwargs)
        return Theme(data)

    def get_weapons(self, *args, **kwargs) -> BaseList[Weapon]:
        data = self.client.get(Endpoints.Weapons, *args, **kwargs)
        return BaseList([Weapon(x) for x in data])

    def search_weapons_by_uuid(self, uuid: str, *args, **kwargs) -> Weapon:
        data = self.client.get(f"{Endpoints.Weapons}/{uuid}", *args, **kwargs)
        return Weapon(data)

    def get_sprays(self, *args, **kwargs) -> BaseList[Spray]:
        data = self.client.get(Endpoints.Sprays, *args, **kwargs)
        return BaseList([Spray(x) for x in data])

    def search_sprays_by_uuid(self, uuid: str, *args, **kwargs) -> Spray:
        data = self.client.get(f"{Endpoints.Sprays}/{uuid}", *args, **kwargs)
        return Spray(data)

    def get_version(self, *args, **kwargs) -> Version:
        data = self.client.get(f"{Endpoints.Version}", *args, **kwargs)
        return Version(data)

    def get_competitivetiers(self, *args, **kwargs) -> BaseList[CompetitiveTier]:
        data = self.client.get(Endpoints.CompetitiveTiers, *args, **kwargs)
        return BaseList([CompetitiveTier(x) for x in data])

    def search_competitivetiers_by_uuid(self, uuid: str, *args, **kwargs) -> CompetitiveTier:
        data = self.client.get(f"{Endpoints.CompetitiveTiers}/{uuid}", *args, **kwargs)
        return CompetitiveTier(data)

    def get_competitive(self, *args, **kwargs) -> BaseList[Competitive]:
        data = self.client.get(Endpoints.Competitive, *args, **kwargs)
        return BaseList([Competitive(x) for x in data])
    
    def search_competitive_by_uuid(self, uuid: str, *args, **kwargs) -> BaseList[Competitive]:
        data = self.client.get(f"{Endpoints.Competitive}/{uuid}", *args, **kwargs)
        return Competitive(data)

    def get_weapon_skins(self, *args, **kwargs) -> BaseList[Skin]:
        data = self.client.get(Endpoints.WeaponSkins, *args, **kwargs)
        return BaseList([Skin(x) for x in data])

    def search_weapon_skins_by_uuid(self, uuid: str, *args, **kwargs):
        data = self.client.get(f"{Endpoints.WeaponSkins}/{uuid}", *args, **kwargs)
        return Skin(data)

    def get_weapons_levels(self, *args, **kwargs) -> BaseList[Level]:
        data = self.client.get(Endpoints.WeaponSkinLevels, *args, **kwargs)
        return BaseList([Level(x) for x in data])

    def search_weapon_levels_by_uuid(self, uuid: str, *args, **kwargs) -> Level:
        data = self.client.get(f"{Endpoints.WeaponSkinLevels}/{uuid}", *args, **kwargs)
        return Level(data)

    def get_weapon_chromas(self, *args, **kwargs) -> BaseList[Chroma]:
        data = self.client.get(Endpoints.WeaponSkinChromas, *args, **kwargs)
        return BaseList([Chroma(x) for x in data])

    def search_weapon_chromas_by_uuid(self, uuid: str, *args, **kwargs) -> Chroma:
        data = self.client.get(f"{Endpoints.WeaponSkinChromas}/{uuid}", *args, **kwargs)
        return Chroma(data)

    def get_contracts(self, *args, **kwargs) -> BaseList[Contract]:
        data = self.client.get(Endpoints.Contracts, *args, **kwargs)
        return BaseList([Contract(x) for x in data])

    def search_contracts_by_uuid(self, uuid: str, *args, **kwargs) -> Chroma:
        data = self.client.get(f"{Endpoints.Contracts}/{uuid}", *args, **kwargs)
        return Contract(data)

    def get_events(self, *args, **kwargs) -> BaseList[Event]:
        data = self.client.get(Endpoints.Events, *args, **kwargs)
        return BaseList([Event(x) for x in data])

    def search_events_by_uuid(self, uuid: str, *args, **kwargs) -> Event:
        data = self.client.get(f"{Endpoints.Events}/{uuid}", *args, **kwargs)
        return Contract(data)

    def get_gears(self, *args, **kwargs) -> BaseList[Gear]:
        data = self.client.get(Endpoints.Gears, *args, **kwargs)
        return BaseList([Gear(x) for x in data])

    def search_gears_by_uuid(self, uuid: str, *args, **kwargs) -> Gear:
        data = self.client.get(f"{Endpoints.Gears}/{uuid}", *args, **kwargs)
        return Gear(data)

    def get_buddy_levels(self, *args, **kwargs) -> BaseList[BuddyLevel]:
        data = self.client.get(Endpoints.BuddyLevels, *args, **kwargs)
        return BaseList([BuddyLevel(x) for x in data])

    def search_buddy_levels_by_uuid(self, uuid: str, *args, **kwargs) -> BuddyLevel:
        data = self.client.get(f"{Endpoints.BuddyLevels}/{uuid}", *args, **kwargs)
        return BuddyLevel(data)

    def get_spray_levels(self, *args, **kwargs) -> BaseList[SprayLevel]:
        data = self.client.get(Endpoints.SprayLevels, *args, **kwargs)
        return BaseList([SprayLevel(x) for x in data])

    def search_spray_levels_by_uuid(self, uuid: str, *args, **kwargs) -> SprayLevel:
        data = self.client.get(f"{Endpoints.SprayLevels}/{uuid}", *args, **kwargs)
        return SprayLevel(data)

    def get_level_borders(self, *args, **kwargs) -> BaseList[LevelBorder]:
        data = self.client.get(Endpoints.LevelBorders, *args, **kwargs)
        return BaseList([LevelBorder(x) for x in data])

    def search_level_borders_by_uuid(self, uuid: str, *args, **kwargs) -> LevelBorder:
        data = self.client.get(f"{Endpoints.LevelBorders}/{uuid}", *args, **kwargs)
        return LevelBorder(data)

class AsyncValorantApi:
    """
Asynchronous valorant-api wrapper
    """

    headers: dict
    client: AsyncClient
    params: dict = {}

    def __init__(self, headers=None, language: str = "en-US"):
        if headers is None:
            headers = {}
        self.params["language"] = language
        self.headers = headers
        self.client = AsyncClient(headers, params=self.params)

    async def get_agents(self, *args, **kwargs) -> BaseList[Agent]:
        data = await self.client.get(Endpoints.Agents, *args, **kwargs)
        return BaseList([Agent(x) for x in data])

    async def search_agents_by_uuid(self, uuid: str, *args, **kwargs) -> Agent:
        data = await self.client.get(f"{Endpoints.Agents}/{uuid}", *args, **kwargs)
        return Agent(data)

    async def get_buddies(self, *args, **kwargs) -> BaseList[Buddy]:
        data = await self.client.get(Endpoints.Buddies, *args, **kwargs)
        return BaseList([Buddy(x) for x in data])

    async def search_buddies_by_uuid(self, uuid: str, *args, **kwargs) -> Buddy:
        data = await self.client.get(f"{Endpoints.Buddies}/{uuid}", *args, **kwargs)
        return Buddy(data)

    async def get_bundles(self, *args, **kwargs) -> BaseList[Bundle]:
        data = await self.client.get(Endpoints.Bundles, *args, **kwargs)
        return BaseList([Bundle(x) for x in data])

    async def search_bundles_by_uuid(self, uuid: str, *args, **kwargs) -> Bundle:
        data = await self.client.get(f"{Endpoints.Bundles}/{uuid}", *args, **kwargs)
        return Bundle(data)

    async def get_contenttiers(self, *args, **kwargs) -> BaseList[ContentTier]:
        data = await self.client.get(Endpoints.ContentTiers, *args, **kwargs)
        return BaseList([ContentTier(x) for x in data])

    async def search_contenttier_by_uuid(self, uuid: str, *args, **kwargs) -> ContentTier:
        data = await self.client.get(f"{Endpoints.ContentTiers}/{uuid}", *args, **kwargs)
        return ContentTier(data)

    async def get_currencies(self, *args, **kwargs) -> BaseList[Currency]:
        data = await self.client.get(Endpoints.Currencies, *args, **kwargs)
        return BaseList([Currency(x) for x in data])

    async def search_currencies_by_uuid(self, uuid: str, *args, **kwargs) -> ContentTier:
        data = await self.client.get(f"{Endpoints.Currencies}/{uuid}", *args, **kwargs)
        return ContentTier(data)

    async def get_ceremonies(self, *args, **kwargs) -> BaseList[Ceremony]:
        data = await self.client.get(Endpoints.Ceremonies, *args, **kwargs)
        return BaseList([Ceremony(x) for x in data])

    async def search_ceremonies_by_uuid(self, uuid: str, *args, **kwargs) -> Ceremony:
        data = await self.client.get(f"{Endpoints.Ceremonies}/{uuid}", *args, **kwargs)
        return Ceremony(data)

    async def get_gamemodes(self, *args, **kwargs) -> BaseList[GameMode]:
        data = await self.client.get(Endpoints.GameMode, *args, **kwargs)
        return BaseList([GameMode(x) for x in data])

    async def search_gamemodes_by_uuid(self, uuid: str, *args, **kwargs) -> GameMode:
        data = await self.client.get(f"{Endpoints.GameMode}/{uuid}", *args, **kwargs)
        return GameMode(data)

    async def get_gamemode_equippables(self, *args, **kwargs) -> BaseList[Equippable]:
        data = await self.client.get(Endpoints.GamemodeEquippables, *args, **kwargs)
        return BaseList([Equippable(x) for x in data])

    async def search_gamemode_equippables_by_uuid(self, uuid: str, *args, **kwargs) -> Equippable:
        data = await self.client.get(f"{Endpoints.GamemodeEquippables}/{uuid}", *args, **kwargs)
        return Equippable(data)

    async def get_maps(self, *args, **kwargs) -> BaseList[Map]:
        data = await self.client.get(Endpoints.Maps, *args, **kwargs)
        return BaseList([Map(x) for x in data])

    async def search_maps_by_uuid(self, uuid: str, *args, **kwargs) -> Map:
        data = await self.client.get(f"{Endpoints.Maps}/{uuid}", *args, **kwargs)
        return Map(data)

    async def get_playercards(self, *args, **kwargs) -> BaseList[PlayerCard]:
        data = await self.client.get(Endpoints.PlayerCards, *args, **kwargs)
        return BaseList([PlayerCard(x) for x in data])

    async def search_playercards_by_uuid(self, uuid: str, *args, **kwargs) -> PlayerCard:
        data = await self.client.get(f"{Endpoints.PlayerCards}/{uuid}", *args, **kwargs)
        return PlayerCard(data)

    async def get_playertitles(self, *args, **kwargs) -> BaseList[PlayerTitle]:
        data = await self.client.get(Endpoints.PlayerTitles, *args, **kwargs)
        return BaseList([PlayerTitle(x) for x in data])

    async def search_playertitles_by_uuid(self, uuid: str, *args, **kwargs) -> PlayerTitle:
        data = await self.client.get(f"{Endpoints.PlayerTitles}/{uuid}", *args, **kwargs)
        return PlayerTitle(data)

    async def get_seasons(self, *args, **kwargs) -> BaseList[Season]:
        data = await self.client.get(Endpoints.Seasons, *args, **kwargs)
        return BaseList([Season(x) for x in data])

    async def search_seasons_by_uuid(self, uuid: str, *args, **kwargs) -> Season:
        data = await self.client.get(f"{Endpoints.Seasons}/{uuid}", *args, **kwargs)
        return Season(data)

    async def get_themes(self, *args, **kwargs) -> BaseList[Theme]:
        data = await self.client.get(Endpoints.Themes, *args, **kwargs)
        return BaseList([Theme(x) for x in data])

    async def search_themes_by_uuid(self, uuid: str, *args, **kwargs) -> Theme:
        data = await self.client.get(f"{Endpoints.Themes}/{uuid}", *args, **kwargs)
        return Theme(data)

    async def get_weapons(self, *args, **kwargs) -> BaseList[Weapon]:
        data = await self.client.get(Endpoints.Weapons, *args, **kwargs)
        return BaseList([Weapon(x) for x in data])

    async def search_weapons_by_uuid(self, uuid: str, *args, **kwargs) -> Weapon:
        data = await self.client.get(f"{Endpoints.Weapons}/{uuid}", *args, **kwargs)
        return Weapon(data)

    async def get_sprays(self, *args, **kwargs) -> BaseList[Spray]:
        data = await self.client.get(Endpoints.Sprays, *args, **kwargs)
        return BaseList([Spray(x) for x in data])

    async def search_sprays_by_uuid(self, uuid: str, *args, **kwargs) -> Spray:
        data = await self.client.get(f"{Endpoints.Sprays}/{uuid}", *args, **kwargs)
        return Spray(data)

    async def get_version(self, *args, **kwargs) -> Version:
        data = await self.client.get(f"{Endpoints.Version}", *args, **kwargs)
        return Version(data)

    async def get_competitivetiers(self, *args, **kwargs) -> BaseList[CompetitiveTier]:
        data = await self.client.get(Endpoints.CompetitiveTiers, *args, **kwargs)
        return BaseList([CompetitiveTier(x) for x in data])

    async def search_competitivetiers_by_uuid(self, uuid: str, *args, **kwargs) -> CompetitiveTier:
        data = await self.client.get(f"{Endpoints.CompetitiveTiers}/{uuid}", *args, **kwargs)
        return CompetitiveTier(data)

    async def get_competitive(self, *args, **kwargs) -> BaseList[Competitive]:
        data = await self.client.get(Endpoints.Competitive, *args, **kwargs)
        return BaseList([Competitive(x) for x in data])

    async def search_competitive_by_uuid(self, uuid: str, *args, **kwargs) -> BaseList[Competitive]:
        data = await self.client.get(f"{Endpoints.Competitive}/{uuid}", *args, **kwargs)
        return Competitive(data)

    async def get_weapon_skins(self, *args, **kwargs) -> BaseList[Skin]:
        data = await self.client.get(Endpoints.WeaponSkins, *args, **kwargs)
        return BaseList([Skin(x) for x in data])

    async def search_weapon_skins_by_uuid(self, uuid: str, *args, **kwargs) -> Skin:
        data = await self.client.get(f"{Endpoints.WeaponSkins}/{uuid}", *args, **kwargs)
        return Skin(data)

    async def get_weapons_levels(self, *args, **kwargs) -> BaseList[Level]:
        data = await self.client.get(Endpoints.WeaponSkinLevels, *args, **kwargs)
        return BaseList([Level(x) for x in data])

    async def search_weapon_levels_by_uuid(self, uuid: str, *args, **kwargs) -> Level:
        data = await self.client.get(f"{Endpoints.WeaponSkinLevels}/{uuid}", *args, **kwargs)
        return Level(data)

    async def get_weapon_chromas(self, *args, **kwargs) -> BaseList[Chroma]:
        data = await self.client.get(Endpoints.WeaponSkinChromas, *args, **kwargs)
        return BaseList([Chroma(x) for x in data])

    async def search_weapon_chromas_by_uuid(self, uuid: str, *args, **kwargs) -> Chroma:
        data = await self.client.get(f"{Endpoints.WeaponSkinChromas}/{uuid}", *args, **kwargs)
        return Chroma(data)

    async def get_contracts(self, *args, **kwargs) -> BaseList[Contract]:
        data = await self.client.get(Endpoints.Contracts, *args, **kwargs)
        return BaseList([Contract(x) for x in data])

    async def search_contracts_by_uuid(self, uuid: str, *args, **kwargs) -> Chroma:
        data = await self.client.get(f"{Endpoints.Contracts}/{uuid}", *args, **kwargs)
        return Contract(data)

    async def get_events(self, *args, **kwargs) -> BaseList[Event]:
        data = await self.client.get(Endpoints.Events, *args, **kwargs)
        return BaseList([Event(x) for x in data])

    async def search_events_by_uuid(self, uuid: str, *args, **kwargs) -> Event:
        data = await self.client.get(f"{Endpoints.Events}/{uuid}", *args, **kwargs)
        return Contract(data)

    async def get_gears(self, *args, **kwargs) -> BaseList[Gear]:
        data = await self.client.get(Endpoints.Gears, *args, **kwargs)
        return BaseList([Gear(x) for x in data])

    async def search_gears_by_uuid(self, uuid: str, *args, **kwargs) -> Gear:
        data = await self.client.get(f"{Endpoints.Gears}/{uuid}", *args, **kwargs)
        return Gear(data)

    async def get_buddy_levels(self, *args, **kwargs) -> BaseList[BuddyLevel]:
        data = await self.client.get(Endpoints.BuddyLevels, *args, **kwargs)
        return BaseList([BuddyLevel(x) for x in data])

    async def search_buddy_levels_by_uuid(self, uuid: str, *args, **kwargs) -> BuddyLevel:
        data = await self.client.get(f"{Endpoints.BuddyLevels}/{uuid}", *args, **kwargs)
        return BuddyLevel(data)

    async def get_spray_levels(self, *args, **kwargs) -> BaseList[SprayLevel]:
        data = await self.client.get(Endpoints.SprayLevels, *args, **kwargs)
        return BaseList([SprayLevel(x) for x in data])

    async def search_spray_levels_by_uuid(self, uuid: str, *args, **kwargs) -> SprayLevel:
        data = await self.client.get(f"{Endpoints.SprayLevels}/{uuid}", *args, **kwargs)
        return SprayLevel(data)

    async def get_level_borders(self, *args, **kwargs) -> BaseList[LevelBorder]:
        data = await self.client.get(Endpoints.LevelBorders, *args, **kwargs)
        return BaseList([LevelBorder(x) for x in data])

    async def search_level_borders_by_uuid(self, uuid: str, *args, **kwargs) -> LevelBorder:
        data = await self.client.get(f"{Endpoints.LevelBorders}/{uuid}", *args, **kwargs)
        return LevelBorder(data)