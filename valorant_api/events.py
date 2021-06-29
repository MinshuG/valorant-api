from dataclasses import dataclass
from datetime import datetime
from valorant_api.utils import Mapper


@dataclass
class Event(Mapper):
    uuid: str
    display_name: str
    short_display_name: str
    start_time: datetime
    end_time: datetime
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.raw_data = data
        self.map(childclasses={})
