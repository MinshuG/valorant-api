from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Level:
    uuid: str
    charm_level: int
    display_name: Optional[str]
    display_icon: Optional[str]
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.charm_level = data.get("charmLevel")
        self.display_name = data.get("displayName")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")


@dataclass
class Buddy:
    uuid: str
    display_name: str
    is_hidden_if_not_owned: bool
    theme_uuid: None
    display_icon: str
    asset_path: str
    levels: List[Level]
    raw_data: dict

    def __init__(self, data: dict):
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.is_hidden_if_not_owned = data.get("isHiddenIfNotOwned")
        self.theme_uuid = data.get("themeUuid")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.levels = [Level(x) for x in data.get("levels")]
        self.raw_data = data
