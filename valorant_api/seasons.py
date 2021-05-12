from dataclasses import dataclass
from datetime import datetime
from typing import Union

import dateutil.parser


@dataclass
class Season:
    uuid: str
    display_name: str
    type: Union[str, None]
    start_time: datetime
    end_time: datetime
    parent_uuid: Union[str, None]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.type = data.get("type")
        self.start_time = dateutil.parser.parse(data.get("startTime"))
        self.end_time = dateutil.parser.parse(data.get("endTime"))
        self.parent_uuid = data.get("parentUuid")
        self.asset_path = data.get("assetPath")
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
