from dataclasses import dataclass
from datetime import datetime

import dateutil.parser


@dataclass
class Version:
    manifest_id: str
    branch: str
    version: str
    build_version: str
    build_date: datetime
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.manifest_id = data.get("manifestId")
        self.branch = data.get("branch")
        self.version = data.get("version")
        self.build_version = data.get("buildVersion")
        self.build_date = dateutil.parser.parse(data.get("buildDate"))
        self.raw_data = data
