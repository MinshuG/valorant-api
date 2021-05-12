from dataclasses import dataclass


@dataclass
class ContentTier:
    uuid: str
    dev_name: str
    highlight_color: str
    display_icon: str
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict):
        self.uuid = data.get("uuid")
        self.dev_name = data.get("devName")
        self.highlight_color = data.get("highlightColor")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data
