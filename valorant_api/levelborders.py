from dataclasses import dataclass


@dataclass
class LevelBorder:
    uuid: str
    starting_level: int
    level_number_appearance: str
    small_player_card_appearance: str
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.starting_level = data.get("startingLevel")
        self.level_number_appearance = data.get("levelNumberAppearance")
        self.small_player_card_appearance = data.get("smallPlayerCardAppearance")
        self.asset_path = data.get("assetPath")
