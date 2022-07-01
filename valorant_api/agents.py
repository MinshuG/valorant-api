from dataclasses import dataclass
from typing import List, Optional


@dataclass
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


@dataclass
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


@dataclass
class Media:
    id: str
    wwise: str
    wave: str

    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.wwise = data.get("wwise")
        self.wave = data.get("wave")


@dataclass
class VoiceLine:
    min_duration: float
    max_duration: float
    media_list: List[Media]

    def __init__(self, data: dict) -> None:
        self.min_duration = data.get("minDuration")
        self.max_duration = data.get("maxDuration")
        self.media_list = [Media(x) for x in data.get("mediaList")]

@dataclass
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
    full_portraitV2: str
    kill_feed_portrait: str
    background: str
    background_gradient_colors: List[str]
    asset_path: str
    is_full_portrait_right_facing: bool
    is_playable_character: bool
    is_available_for_test: bool
    role: Optional[Role]
    abilities: Optional[List[Ability]]
    voice_line: Optional[VoiceLine]
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
        self.full_portraitV2 = data.get("fullPortraitV2")
        self.kill_feed_portrait = data.get("killfeedPortrait")
        self.background = data.get("background")
        self.background_gradient_colors = data.get("backgroundGradientColors")
        self.asset_path = data.get("assetPath")
        self.is_full_portrait_right_facing = data.get("isFullPortraitRightFacing")
        self.is_playable_character = data.get("isPlayableCharacter")
        self.is_available_for_test = data.get("isAvailableForTest")
        self.role = Role(data.get("role")) if data.get("role") is not None else None
        self.abilities = [Ability(x) for x in data.get("abilities")] if data.get("abilities") is not None else None
        self.voice_line = VoiceLine(data.get("voiceLine")) if data.get("voiceLine") is not None else None
        self.raw_data = data
