from dataclasses import dataclass
from typing import Union


@dataclass
class Theme:
    uuid: str
    display_name: str
    display_icon: Union[str, None]
    store_featured_image: Union[str, None]
    asset_path: str
    raw_data: dict

    def __init__(self, obj: dict) -> None:
        self.uuid = obj.get("uuid")
        self.display_name = obj.get("displayName")
        self.display_icon = obj.get("displayIcon")
        self.store_featured_image = obj.get("storeFeaturedImage")
        self.asset_path = obj.get("assetPath")
        self.raw_data = obj
