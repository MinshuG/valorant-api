from dataclasses import dataclass
from typing import Optional


@dataclass
class Bundle:
    uuid: str
    display_name: str
    display_name_sub_text: Optional[str]
    description: str
    display_icon: str
    display_icon2: str
    vertical_promo_image: Optional[str]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.display_name_sub_text = data.get("displayNameSubText")
        self.description = data.get("description")
        self.display_icon = data.get("displayIcon")
        self.display_icon2 = data.get("displayIcon2")
        self.vertical_promo_image = data.get("verticalPromoImage")
        self.asset_path = data.get("assetPath")
        self.raw_data = data
