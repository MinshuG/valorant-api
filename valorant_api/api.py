from typing import NewType

from valorant_api.spray import Spray
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
from .weapons import Weapon

# BaseList = NewType('BaseList', BaseList)


class SyncValorantApi:
    """
Synchronous valorant-api wrapper
    """

    headers: dict
    sync: SyncClient
    params: dict = {}

    def __init__(self, headers=None, language: str = "en-US"):
        if headers is None:
            headers = {}
        self.params["language"] = language
        self.headers = headers
        self.sync = SyncClient(headers, params=self.params)

    def get_agents(self) -> BaseList[Agent]:
        data = self.sync.get(Endpoints.Agents)
        return BaseList([Agent(x) for x in data])

    def search_agents_by_uuid(self, uuid: str) -> Agent:
        data = self.sync.get(f"{Endpoints.Agents}/{uuid}")
        return Agent(data)

    def get_buddies(self) -> BaseList[Buddy]:
        data = self.sync.get(Endpoints.Buddies)
        return BaseList([Buddy(x) for x in data])

    def search_buddies_by_uuid(self, uuid: str) -> Buddy:
        data = self.sync.get(f"{Endpoints.Buddies}/{uuid}")
        return Buddy(data)

    def get_bundles(self) -> BaseList[Bundle]:
        data = self.sync.get(Endpoints.Bundles)
        return BaseList([Bundle(x) for x in data])

    def search_bundles_by_uuid(self, uuid: str) -> Bundle:
        data = self.sync.get(f"{Endpoints.Bundles}/{uuid}")
        return Bundle(data)

    def get_contenttiers(self) -> BaseList[ContentTier]:
        data = self.sync.get(Endpoints.Content_Tiers)
        return BaseList([ContentTier(x) for x in data])

    def search_contenttier_by_uuid(self, uuid: str) -> ContentTier:
        data = self.sync.get(f"{Endpoints.Content_Tiers}/{uuid}")
        return ContentTier(data)

    def get_currencies(self) -> BaseList[Currency]:
        data = self.sync.get(Endpoints.Currencies)
        return BaseList([Currency(x) for x in data])

    def search_currencies_by_uuid(self, uuid: str) -> ContentTier:
        data = self.sync.get(f"{Endpoints.Currencies}/{uuid}")
        return ContentTier(data)

    def get_gamemodes(self) -> BaseList[GameMode]:
        data = self.sync.get(Endpoints.GameMode)
        return BaseList([GameMode(x) for x in data])

    def search_gamemodes_by_uuid(self, uuid: str) -> GameMode:
        data = self.sync.get(f"{Endpoints.GameMode}/{uuid}")
        return GameMode(data)

    def get_gamemode_equippables(self) -> BaseList[Equippable]:
        data = self.sync.get(Endpoints.GamemodeEquippables)
        return BaseList([Equippable(x) for x in data])

    def search_gamemode_equippables_by_uuid(self, uuid: str) -> Equippable:
        data = self.sync.get(f"{Endpoints.GamemodeEquippables}/{uuid}")
        return Equippable(data)

    def get_maps(self) -> BaseList[Map]:
        data = self.sync.get(Endpoints.Maps)
        return BaseList([Map(x) for x in data])

    def search_maps_by_uuid(self, uuid: str) -> Map:
        data = self.sync.get(f"{Endpoints.Maps}/{uuid}")
        return Map(data)

    def get_playercards(self) -> BaseList[PlayerCard]:
        data = self.sync.get(Endpoints.PlayerCards)
        return BaseList([PlayerCard(x) for x in data])

    def search_playercards_by_uuid(self, uuid: str) -> PlayerCard:
        data = self.sync.get(f"{Endpoints.PlayerCards}/{uuid}")
        return PlayerCard(data)

    def get_playertitles(self) -> BaseList[PlayerTitle]:
        data = self.sync.get(Endpoints.PlayerTitles)
        return BaseList([PlayerTitle(x) for x in data])

    def search_playertitles_by_uuid(self, uuid: str) -> PlayerTitle:
        data = self.sync.get(f"{Endpoints.PlayerTitles}/{uuid}")
        return PlayerTitle(data)

    def get_seasons(self) -> BaseList[Season]:
        data = self.sync.get(Endpoints.Seasons)
        return BaseList([Season(x) for x in data])

    def search_seasons_by_uuid(self, uuid: str) -> Season:
        data = self.sync.get(f"{Endpoints.Seasons}/{uuid}")
        return Season(data)

    def get_themes(self) -> BaseList[Theme]:
        data = self.sync.get(Endpoints.Themes)
        return BaseList([Theme(x) for x in data])

    def search_themes_by_uuid(self, uuid: str) -> Theme:
        data = self.sync.get(f"{Endpoints.Themes}/{uuid}")
        return Theme(data)

    def get_weapons(self) -> BaseList[Weapon]:
        data = self.sync.get(Endpoints.Weapons)
        return BaseList([Weapon(x) for x in data])

    def search_weapons_by_uuid(self, uuid: str) -> Weapon:
        data = self.sync.get(f"{Endpoints.Weapons}/{uuid}")
        return Weapon(data)

    def get_sprays(self) -> BaseList[Spray]:
        data = self.sync.get(Endpoints.Sprays)
        return BaseList([Spray(x) for x in data])

    def search_sprays_by_uuid(self, uuid: str) -> Spray:
        data = self.sync.get(f"{Endpoints.Sprays}/{uuid}")
        return Spray(data)

    def get_version(self) -> Version:
        data = self.sync.get(f"{Endpoints.Version}")
        return Version(data)


class AsyncValorantApi:
    """
Asynchronous valorant-api wrapper
    """

    headers: dict
    Async: AsyncClient
    params: dict = {}

    def __init__(self, headers=None, language: str = "en-US"):
        if headers is None:
            headers = {}
        self.params["language"] = language
        self.headers = headers
        self.Async = AsyncClient(headers, params=self.params)

    async def get_agents(self) -> BaseList[Agent]:
        data = await self.Async.get(Endpoints.Agents)
        return BaseList([Agent(x) for x in data])

    async def search_agents_by_uuid(self, uuid: str) -> Agent:
        data = await self.Async.get(f"{Endpoints.Agents}/{uuid}")
        return Agent(data)

    async def get_buddies(self) -> BaseList[Buddy]:
        data = await self.Async.get(Endpoints.Buddies)
        return BaseList([Buddy(x) for x in data])

    async def search_buddies_by_uuid(self, uuid: str) -> Buddy:
        data = await self.Async.get(f"{Endpoints.Buddies}/{uuid}")
        return Buddy(data)

    async def get_bundles(self) -> BaseList[Bundle]:
        data = await self.Async.get(Endpoints.Bundles)
        return BaseList([Bundle(x) for x in data])

    async def search_bundles_by_uuid(self, uuid: str) -> Bundle:
        data = await self.Async.get(f"{Endpoints.Bundles}/{uuid}")
        return Bundle(data)

    async def get_contenttiers(self) -> BaseList[ContentTier]:
        data = await self.Async.get(Endpoints.Content_Tiers)
        return BaseList([ContentTier(x) for x in data])

    async def search_contenttier_by_uuid(self, uuid: str) -> ContentTier:
        data = await self.Async.get(f"{Endpoints.Content_Tiers}/{uuid}")
        return ContentTier(data)

    async def get_currencies(self) -> BaseList[Currency]:
        data = await self.Async.get(Endpoints.Currencies)
        return BaseList([Currency(x) for x in data])

    async def search_currencies_by_uuid(self, uuid: str) -> ContentTier:
        data = await self.Async.get(f"{Endpoints.Currencies}/{uuid}")
        return ContentTier(data)

    async def get_gamemodes(self) -> BaseList[GameMode]:
        data = await self.Async.get(Endpoints.GameMode)
        return BaseList([GameMode(x) for x in data])

    async def search_gamemodes_by_uuid(self, uuid: str) -> GameMode:
        data = await self.Async.get(f"{Endpoints.GameMode}/{uuid}")
        return GameMode(data)

    async def get_gamemode_equippables(self) -> BaseList[Equippable]:
        data = await self.Async.get(Endpoints.GamemodeEquippables)
        return BaseList([Equippable(x) for x in data])

    async def search_gamemode_equippables_by_uuid(self, uuid: str) -> Equippable:
        data = await self.Async.get(f"{Endpoints.GamemodeEquippables}/{uuid}")
        return Equippable(data)

    async def get_maps(self) -> BaseList[Map]:
        data = await self.Async.get(Endpoints.Maps)
        return BaseList([Map(x) for x in data])

    async def search_maps_by_uuid(self, uuid: str) -> Map:
        data = await self.Async.get(f"{Endpoints.Maps}/{uuid}")
        return Map(data)

    async def get_playercards(self) -> BaseList[PlayerCard]:
        data = await self.Async.get(Endpoints.PlayerCards)
        return BaseList([PlayerCard(x) for x in data])

    async def search_playercards_by_uuid(self, uuid: str) -> PlayerCard:
        data = await self.Async.get(f"{Endpoints.PlayerCards}/{uuid}")
        return PlayerCard(data)

    async def get_playertitles(self) -> BaseList[PlayerTitle]:
        data = await self.Async.get(Endpoints.PlayerTitles)
        return BaseList([PlayerTitle(x) for x in data])

    async def search_playertitles_by_uuid(self, uuid: str) -> PlayerTitle:
        data = await self.Async.get(f"{Endpoints.PlayerTitles}/{uuid}")
        return PlayerTitle(data)

    async def get_seasons(self) -> BaseList[Season]:
        data = await self.Async.get(Endpoints.Seasons)
        return BaseList([Season(x) for x in data])

    async def search_seasons_by_uuid(self, uuid: str) -> Season:
        data = await self.Async.get(f"{Endpoints.Seasons}/{uuid}")
        return Season(data)

    async def get_themes(self) -> BaseList[Theme]:
        data = await self.Async.get(Endpoints.Themes)
        return BaseList([Theme(x) for x in data])

    async def search_themes_by_uuid(self, uuid: str) -> Theme:
        data = await self.Async.get(f"{Endpoints.Themes}/{uuid}")
        return Theme(data)

    async def get_weapons(self) -> BaseList[Weapon]:
        data = await self.Async.get(Endpoints.Weapons)
        return BaseList([Weapon(x) for x in data])

    async def search_weapons_by_uuid(self, uuid: str) -> Weapon:
        data = await self.Async.get(f"{Endpoints.Weapons}/{uuid}")
        return Weapon(data)

    async def get_sprays(self) -> BaseList[Spray]:
        data = await self.Async.get(Endpoints.Sprays)
        return BaseList([Spray(x) for x in data])

    async def search_sprays_by_uuid(self, uuid: str) -> Spray:
        data = await self.Async.get(f"{Endpoints.Sprays}/{uuid}")
        return Spray(data)

    async def get_version(self) -> Version:
        data = await self.Async.get(f"{Endpoints.Version}")
        return Version(data)
