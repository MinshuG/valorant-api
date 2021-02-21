from typing import List, Optional


class Ability:
    slot: str
    display_name: str
    description: str
    display_icon: str

    def __init__(self, data: dict) -> None:
        self.slot = data.get("slot")
        self.display_name = data.get("displayName")
        self.description = data.get("description")
        self.display_icon = data.get("displayIcon")


class Role:
    uuid: str
    display_name: str
    description: str
    display_icon: str
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.description = data.get("description")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")


class Agent:
    uuid: str
    display_name: str
    description: str
    developer_name: str
    character_tags: Optional[list]
    display_icon: str
    display_icon_small: str
    bust_portrait: str
    full_portrait: str
    asset_path: str
    is_full_portrait_right_facing: bool
    is_playable_character: bool
    is_available_for_test: bool
    role: Optional[Role]
    abilities: Optional[List[Ability]]
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.description = data.get("description")
        self.developer_name = data.get("developerName")
        self.character_tags = data.get("characterTags")
        self.display_icon = data.get("displayIcon")
        self.display_icon_small = data.get("displayIconSmall")
        self.bust_portrait = data.get("bustPortrait")
        self.full_portrait = data.get("fullPortrait")
        self.asset_path = data.get("assetPath")
        self.is_full_portrait_right_facing = data.get("isFullPortraitRightFacing")
        self.is_playable_character = data.get("isPlayableCharacter")
        self.is_available_for_test = data.get("isAvailableForTest")
        self.role = Role(data.get("role")) if data.get("role") is not None else None
        self.abilities = [Ability(x) for x in data.get("abilities")] if data.get("abilities") is not None else None
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
