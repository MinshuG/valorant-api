from typing import Optional


class Spray:
    uuid: str
    display_name: str
    category: Optional[str]
    display_icon: str
    asset_path: str
    raw_data: dict

    def __init__(self,data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.category = data.get("category")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data
