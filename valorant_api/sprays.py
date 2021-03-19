from typing import Optional, List


class Level:
    uuid: str
    spray_level: int
    display_name: str
    display_icon: str
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.spray_level = data.get("sprayLevel")
        self.display_name = data.get("displayName")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")


class Spray:
    uuid: str
    display_name: str
    category: Optional[str]
    display_icon: str
    full_icon: Optional[str]
    full_transparent_icon: Optional[str]
    asset_path: str
    levels: List[Level]
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.category = data.get("category")
        self.display_icon = data.get("displayIcon")
        self.full_icon = data.get("fullIcon")
        self.full_transparent_icon = data.get("fullTransparentIcon")
        self.asset_path = data.get("assetPath")
        self.levels = [Level(x) for x in data.get("levels")]
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
