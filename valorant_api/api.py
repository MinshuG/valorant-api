from valorant_api.events import Event
from valorant_api.contracts import Contract
from .competitive import Competitive
from .competitivetiers import CompetitiveTier
from .sprays import Spray
from .agents import Agent
from .base_list import BaseList
from .buddies import Buddy
from .bundles import Bundle
from .contenttiers import ContentTier
from .currencies import Currency
from .endpoints import Endpoints
from .gamemodes import GameMode, Equippable
from .httpclient import AsyncClient, SyncClient
from .maps import Map
from .playercards import PlayerCard
from .playertitles import PlayerTitle
from .seasons import Season
from .themes import Theme
from .version import Version
from .weapons import Chroma, Skin, Weapon, Level


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

    def get_agents(self) -> BaseList[Agent]:
        data = self.client.get(Endpoints.Agents)
        return BaseList([Agent(x) for x in data])

    def search_agents_by_uuid(self, uuid: str) -> Agent:
        data = self.client.get(f"{Endpoints.Agents}/{uuid}")
        return Agent(data)

    def get_buddies(self) -> BaseList[Buddy]:
        data = self.client.get(Endpoints.Buddies)
        return BaseList([Buddy(x) for x in data])

    def search_buddies_by_uuid(self, uuid: str) -> Buddy:
        data = self.client.get(f"{Endpoints.Buddies}/{uuid}")
        return Buddy(data)

    def get_bundles(self) -> BaseList[Bundle]:
        data = self.client.get(Endpoints.Bundles)
        return BaseList([Bundle(x) for x in data])

    def search_bundles_by_uuid(self, uuid: str) -> Bundle:
        data = self.client.get(f"{Endpoints.Bundles}/{uuid}")
        return Bundle(data)

    def get_contenttiers(self) -> BaseList[ContentTier]:
        data = self.client.get(Endpoints.ContentTiers)
        return BaseList([ContentTier(x) for x in data])

    def search_contenttier_by_uuid(self, uuid: str) -> ContentTier:
        data = self.client.get(f"{Endpoints.ContentTiers}/{uuid}")
        return ContentTier(data)

    def get_currencies(self) -> BaseList[Currency]:
        data = self.client.get(Endpoints.Currencies)
        return BaseList([Currency(x) for x in data])

    def search_currencies_by_uuid(self, uuid: str) -> ContentTier:
        data = self.client.get(f"{Endpoints.Currencies}/{uuid}")
        return ContentTier(data)

    def get_gamemodes(self) -> BaseList[GameMode]:
        data = self.client.get(Endpoints.GameMode)
        return BaseList([GameMode(x) for x in data])

    def search_gamemodes_by_uuid(self, uuid: str) -> GameMode:
        data = self.client.get(f"{Endpoints.GameMode}/{uuid}")
        return GameMode(data)

    def get_gamemode_equippables(self) -> BaseList[Equippable]:
        data = self.client.get(Endpoints.GamemodeEquippables)
        return BaseList([Equippable(x) for x in data])

    def search_gamemode_equippables_by_uuid(self, uuid: str) -> Equippable:
        data = self.client.get(f"{Endpoints.GamemodeEquippables}/{uuid}")
        return Equippable(data)

    def get_maps(self) -> BaseList[Map]:
        data = self.client.get(Endpoints.Maps)
        return BaseList([Map(x) for x in data])

    def search_maps_by_uuid(self, uuid: str) -> Map:
        data = self.client.get(f"{Endpoints.Maps}/{uuid}")
        return Map(data)

    def get_playercards(self) -> BaseList[PlayerCard]:
        data = self.client.get(Endpoints.PlayerCards)
        return BaseList([PlayerCard(x) for x in data])

    def search_playercards_by_uuid(self, uuid: str) -> PlayerCard:
        data = self.client.get(f"{Endpoints.PlayerCards}/{uuid}")
        return PlayerCard(data)

    def get_playertitles(self) -> BaseList[PlayerTitle]:
        data = self.client.get(Endpoints.PlayerTitles)
        return BaseList([PlayerTitle(x) for x in data])

    def search_playertitles_by_uuid(self, uuid: str) -> PlayerTitle:
        data = self.client.get(f"{Endpoints.PlayerTitles}/{uuid}")
        return PlayerTitle(data)

    def get_seasons(self) -> BaseList[Season]:
        data = self.client.get(Endpoints.Seasons)
        return BaseList([Season(x) for x in data])

    def search_seasons_by_uuid(self, uuid: str) -> Season:
        data = self.client.get(f"{Endpoints.Seasons}/{uuid}")
        return Season(data)

    def get_themes(self) -> BaseList[Theme]:
        data = self.client.get(Endpoints.Themes)
        return BaseList([Theme(x) for x in data])

    def search_themes_by_uuid(self, uuid: str) -> Theme:
        data = self.client.get(f"{Endpoints.Themes}/{uuid}")
        return Theme(data)

    def get_weapons(self) -> BaseList[Weapon]:
        data = self.client.get(Endpoints.Weapons)
        return BaseList([Weapon(x) for x in data])

    def search_weapons_by_uuid(self, uuid: str) -> Weapon:
        data = self.client.get(f"{Endpoints.Weapons}/{uuid}")
        return Weapon(data)

    def get_sprays(self) -> BaseList[Spray]:
        data = self.client.get(Endpoints.Sprays)
        return BaseList([Spray(x) for x in data])

    def search_sprays_by_uuid(self, uuid: str) -> Spray:
        data = self.client.get(f"{Endpoints.Sprays}/{uuid}")
        return Spray(data)

    def get_version(self) -> Version:
        data = self.client.get(f"{Endpoints.Version}")
        return Version(data)

    def get_competitivetiers(self) -> BaseList[CompetitiveTier]:
        data = self.client.get(Endpoints.CompetitiveTiers)
        return BaseList([CompetitiveTier(x) for x in data])

    def search_competitivetiers_by_uuid(self, uuid: str) -> CompetitiveTier:
        data = self.client.get(f"{Endpoints.CompetitiveTiers}/{uuid}")
        return CompetitiveTier(data)

    def get_competitive(self) -> BaseList[Competitive]:
        data = self.client.get(Endpoints.Competitive)
        return BaseList([Competitive(x) for x in data])
    
    def search_competitive_by_uuid(self, uuid: str) -> BaseList[Competitive]:
        data = self.client.get(f"{Endpoints.Competitive}/{uuid}")
        return Competitive(data)

    def get_weapon_skins(self) -> BaseList[Skin]:
        data = self.client.get(Endpoints.WeaponSkins)
        return BaseList([Skin(x) for x in data])

    def search_weapon_skins_by_uuid(self, uuid: str):
        data = self.client.get(f"{Endpoints.WeaponSkins}/{uuid}")
        return Skin(data)

    def get_weapons_levels(self) -> BaseList[Level]:
        data = self.client.get(Endpoints.WeaponSkinLevels)
        return BaseList([Level(x) for x in data])

    def search_weapon_levels_by_uuid(self, uuid: str) -> Level:
        data = self.client.get(f"{Endpoints.WeaponSkinLevels}/{uuid}")
        return Level(data)

    def get_weapon_chromas(self) -> BaseList[Chroma]:
        data = self.client.get(Endpoints.WeaponSkinChromas)
        return BaseList([Chroma(x) for x in data])

    def search_weapon_chromas_by_uuid(self, uuid: str) -> Chroma:
        data = self.client.get(f"{Endpoints.WeaponSkinChromas}/{uuid}")
        return Chroma(data)
    
    def get_contracts(self) -> BaseList[Contract]:
        data = self.client.get(Endpoints.Contracts)
        return BaseList([Contract(x) for x in data])

    def search_contracts_by_uuid(self, uuid: str) -> Chroma:
        data = self.client.get(f"{Endpoints.Contracts}/{uuid}")
        return Contract(data)
    
    def get_events(self) -> BaseList[Event]:
        data = self.client.get(Endpoints.Events)
        return BaseList([Event(x) for x in data])

    def search_events_by_uuid(self, uuid: str) -> Event:
        data = self.client.get(f"{Endpoints.Events}/{uuid}")
        return Contract(data)


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

    async def get_agents(self) -> BaseList[Agent]:
        data = await self.client.get(Endpoints.Agents)
        return BaseList([Agent(x) for x in data])

    async def search_agents_by_uuid(self, uuid: str) -> Agent:
        data = await self.client.get(f"{Endpoints.Agents}/{uuid}")
        return Agent(data)

    async def get_buddies(self) -> BaseList[Buddy]:
        data = await self.client.get(Endpoints.Buddies)
        return BaseList([Buddy(x) for x in data])

    async def search_buddies_by_uuid(self, uuid: str) -> Buddy:
        data = await self.client.get(f"{Endpoints.Buddies}/{uuid}")
        return Buddy(data)

    async def get_bundles(self) -> BaseList[Bundle]:
        data = await self.client.get(Endpoints.Bundles)
        return BaseList([Bundle(x) for x in data])

    async def search_bundles_by_uuid(self, uuid: str) -> Bundle:
        data = await self.client.get(f"{Endpoints.Bundles}/{uuid}")
        return Bundle(data)

    async def get_contenttiers(self) -> BaseList[ContentTier]:
        data = await self.client.get(Endpoints.ContentTiers)
        return BaseList([ContentTier(x) for x in data])

    async def search_contenttier_by_uuid(self, uuid: str) -> ContentTier:
        data = await self.client.get(f"{Endpoints.ContentTiers}/{uuid}")
        return ContentTier(data)

    async def get_currencies(self) -> BaseList[Currency]:
        data = await self.client.get(Endpoints.Currencies)
        return BaseList([Currency(x) for x in data])

    async def search_currencies_by_uuid(self, uuid: str) -> ContentTier:
        data = await self.client.get(f"{Endpoints.Currencies}/{uuid}")
        return ContentTier(data)

    async def get_gamemodes(self) -> BaseList[GameMode]:
        data = await self.client.get(Endpoints.GameMode)
        return BaseList([GameMode(x) for x in data])

    async def search_gamemodes_by_uuid(self, uuid: str) -> GameMode:
        data = await self.client.get(f"{Endpoints.GameMode}/{uuid}")
        return GameMode(data)

    async def get_gamemode_equippables(self) -> BaseList[Equippable]:
        data = await self.client.get(Endpoints.GamemodeEquippables)
        return BaseList([Equippable(x) for x in data])

    async def search_gamemode_equippables_by_uuid(self, uuid: str) -> Equippable:
        data = await self.client.get(f"{Endpoints.GamemodeEquippables}/{uuid}")
        return Equippable(data)

    async def get_maps(self) -> BaseList[Map]:
        data = await self.client.get(Endpoints.Maps)
        return BaseList([Map(x) for x in data])

    async def search_maps_by_uuid(self, uuid: str) -> Map:
        data = await self.client.get(f"{Endpoints.Maps}/{uuid}")
        return Map(data)

    async def get_playercards(self) -> BaseList[PlayerCard]:
        data = await self.client.get(Endpoints.PlayerCards)
        return BaseList([PlayerCard(x) for x in data])

    async def search_playercards_by_uuid(self, uuid: str) -> PlayerCard:
        data = await self.client.get(f"{Endpoints.PlayerCards}/{uuid}")
        return PlayerCard(data)

    async def get_playertitles(self) -> BaseList[PlayerTitle]:
        data = await self.client.get(Endpoints.PlayerTitles)
        return BaseList([PlayerTitle(x) for x in data])

    async def search_playertitles_by_uuid(self, uuid: str) -> PlayerTitle:
        data = await self.client.get(f"{Endpoints.PlayerTitles}/{uuid}")
        return PlayerTitle(data)

    async def get_seasons(self) -> BaseList[Season]:
        data = await self.client.get(Endpoints.Seasons)
        return BaseList([Season(x) for x in data])

    async def search_seasons_by_uuid(self, uuid: str) -> Season:
        data = await self.client.get(f"{Endpoints.Seasons}/{uuid}")
        return Season(data)

    async def get_themes(self) -> BaseList[Theme]:
        data = await self.client.get(Endpoints.Themes)
        return BaseList([Theme(x) for x in data])

    async def search_themes_by_uuid(self, uuid: str) -> Theme:
        data = await self.client.get(f"{Endpoints.Themes}/{uuid}")
        return Theme(data)

    async def get_weapons(self) -> BaseList[Weapon]:
        data = await self.client.get(Endpoints.Weapons)
        return BaseList([Weapon(x) for x in data])

    async def search_weapons_by_uuid(self, uuid: str) -> Weapon:
        data = await self.client.get(f"{Endpoints.Weapons}/{uuid}")
        return Weapon(data)

    async def get_sprays(self) -> BaseList[Spray]:
        data = await self.client.get(Endpoints.Sprays)
        return BaseList([Spray(x) for x in data])

    async def search_sprays_by_uuid(self, uuid: str) -> Spray:
        data = await self.client.get(f"{Endpoints.Sprays}/{uuid}")
        return Spray(data)

    async def get_version(self) -> Version:
        data = await self.client.get(f"{Endpoints.Version}")
        return Version(data)

    async def get_competitivetiers(self) -> BaseList[CompetitiveTier]:
        data = await self.client.get(Endpoints.CompetitiveTiers)
        return BaseList([CompetitiveTier(x) for x in data])

    async def search_competitivetiers_by_uuid(self, uuid: str) -> CompetitiveTier:
        data = await self.client.get(f"{Endpoints.CompetitiveTiers}/{uuid}")
        return CompetitiveTier(data)
    
    async def get_competitive(self) -> BaseList[Competitive]:
        data = await self.client.get(Endpoints.Competitive)
        return BaseList([Competitive(x) for x in data])
    
    async def search_competitive_by_uuid(self, uuid: str) -> BaseList[Competitive]:
        data = await self.client.get(f"{Endpoints.Competitive}/{uuid}")
        return Competitive(data)

    async def get_weapon_skins(self) -> BaseList[Skin]:
        data = await self.client.get(Endpoints.WeaponSkins)
        return BaseList([Skin(x) for x in data])

    async def search_weapon_skins_by_uuid(self, uuid: str) -> Skin:
        data = await self.client.get(f"{Endpoints.WeaponSkins}/{uuid}")
        return Skin(data)

    async def get_weapons_levels(self) -> BaseList[Level]:
        data = await self.client.get(Endpoints.WeaponSkinLevels)
        return BaseList([Level(x) for x in data])

    async def search_weapon_levels_by_uuid(self, uuid: str) -> Level:
        data = await self.client.get(f"{Endpoints.WeaponSkinLevels}/{uuid}")
        return Level(data)

    async def get_weapon_chromas(self) -> BaseList[Chroma]:
        data = await self.client.get(Endpoints.WeaponSkinChromas)
        return BaseList([Chroma(x) for x in data])

    async def search_weapon_chromas_by_uuid(self, uuid: str) -> Chroma:
        data = await self.client.get(f"{Endpoints.WeaponSkinChromas}/{uuid}")
        return Chroma(data)

    async def get_contracts(self) -> BaseList[Contract]:
        data = await self.client.get(Endpoints.Contracts)
        return BaseList([Contract(x) for x in data])

    async def search_contracts_by_uuid(self, uuid: str) -> Chroma:
        data = await self.client.get(f"{Endpoints.Contracts}/{uuid}")
        return Contract(data)

    async def get_events(self) -> BaseList[Event]:
        data = await self.client.get(Endpoints.Events)
        return BaseList([Event(x) for x in data])

    async def search_events_by_uuid(self, uuid: str) -> Event:
        data = await self.client.get(f"{Endpoints.Events}/{uuid}")
        return Contract(data)
