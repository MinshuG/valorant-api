from datetime import datetime

import dateutil.parser


class Version:
    branch: str
    version: str
    build_version: str
    build_date: datetime
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.branch = data.get("branch")
        self.version = data.get("version")
        self.build_version = data.get("buildVersion")
        self.build_date = dateutil.parser.parse(data.get("buildDate"))
        self.raw_data = data
