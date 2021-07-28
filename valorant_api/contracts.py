from enum import Enum
from dataclasses import dataclass
from typing import List
from .utils import Mapper

# class TypeEnum(Enum):
#     CURRENCY = "Currency"
#     EQUIPPABLE_CHARM_LEVEL = "EquippableCharmLevel"
#     EQUIPPABLE_SKIN_LEVEL = "EquippableSkinLevel"
#     PLAYER_CARD = "PlayerCard"
#     SPRAY = "Spray"
#     TITLE = "Title"


@dataclass
class Reward(Mapper):
    type: str
    uuid: str
    amount: int
    is_highlighted: bool

    def __init__(self):
        super().__init__()

@dataclass
class Level(Mapper):
    reward: Reward
    xp: int
    vp_cost: int
    is_purchasable_with_vp: bool

    def __init__(self):
        super().__init__()

@dataclass
class Chapter(Mapper):
    is_epilogue: bool
    levels: List[Level]
    free_rewards: List[Reward]

    def __init__(self):
        super().__init__()

@dataclass
class Content(Mapper):
    relation_uuid: str
    relation_type: str
    chapters: List[Chapter]
    premium_reward_schedule_uuid: str
    premium_vp_cost: int

    def __init__(self):
        super().__init__()

@dataclass
class Contract(Mapper):
    uuid: str
    display_name: str
    display_icon: str
    ship_it: bool
    free_reward_schedule_uuid: str
    content: Content
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.raw_data = data
        self.map(childclasses={"content": Content, "chapters": Chapter, "levels": Level, "reward": Reward, "freeRewards": Reward})

