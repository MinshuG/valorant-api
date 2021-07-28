from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Tier:
    tier: int
    tier_name: str
    division: str
    division_name: str
    background_color: str
    color: str
    small_icon: Optional[str]
    large_icon: Optional[str]
    rank_triangle_down_icon: Optional[str]
    rank_triangle_up_icon: Optional[str]

    def __init__(self, data: dict) -> None:
        self.tier = data.get("tier")
        self.tier_name = data.get("tierName")
        self.division = data.get("division")
        self.division_name = data.get("divisionName")
        self.background_color = data.get("backgroundColor")
        self.color = data.get("color")
        self.small_icon = data.get("smallIcon")
        self.large_icon = data.get("largeIcon")
        self.rank_triangle_down_icon = data.get("rankTriangleDownIcon")
        self.rank_triangle_up_icon = data.get("rankTriangleUpIcon")


@dataclass
class CompetitiveTier:
    uuid: str
    asset_object_name: str
    tiers: Optional[List[Tier]]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.asset_object_name = data.get("assetObjectName")
        self.tiers = [Tier(x) for x in data.get("tiers")] if data.get("tiers") is not None else None
        self.asset_path = data.get("assetPath")
