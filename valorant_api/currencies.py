from dataclasses import dataclass
from typing import Union


@dataclass
class Currency:
    uuid: str
    display_name: str
    display_name_singular: str
    display_icon: str
    large_icon: Union[str, None]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict):
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.display_name_singular = data.get("displayNameSingular")
        self.display_icon = data.get("displayIcon")
        self.large_icon = data.get("largeIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data
