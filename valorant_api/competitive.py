from dataclasses import dataclass
from typing import List, Optional
from .utils import Mapper


@dataclass
class Border(Mapper):
    uuid: str
    level: int
    wins_required: int
    display_icon: str
    small_icon: Optional[str]
    asset_path: str

    def __init__(self):
        super().__init__()


@dataclass
class Competitive(Mapper):
    uuid: str
    start_time: str
    end_time: str
    season_uuid: str
    competitive_tiers_uuid: str
    borders: List[Border]
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.raw_data = data
        self.map(childclasses={"borders": Border})
