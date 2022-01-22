from dataclasses import dataclass


@dataclass
class Ceremony:
    uuid: str
    display_name: str
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get('uuid')
        self.display_name = data.get('displayName')
        self.asset_path = data.get('assetPath')
