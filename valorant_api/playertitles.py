from dataclasses import dataclass


@dataclass
class PlayerTitle:
    uuid: str
    display_name: str
    title_text: str  # same as displayName but without the " Title" suffix
    isb_hidden_if_not_owned: bool
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.title_text = data.get("titleText")
        self.isb_hidden_if_not_owned = data.get("isbHiddenIfNotOwned")
        self.asset_path = data.get("assetPath")
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
