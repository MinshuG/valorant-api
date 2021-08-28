from dataclasses import dataclass
from typing import List



@dataclass
class Location:
    x: float
    y: float

    def __init__(self, data: dict) -> None:
        self.x = data.get('x')
        self.y = data.get('y')


@dataclass
class Callout:
    region_name: str
    super_region_name: str
    location: Location

    def __init__(self, data: dict) -> None:
        self.region_name = data.get("regionName")
        self.super_region_name = data.get("superRegionName")
        self.location = Location(data.get("location"))


@dataclass
class Map:
    uuid: str
    display_name: str
    coordinates: str
    display_icon: str
    list_view_icon: str
    splash: str
    asset_path: str
    map_url: str
    x_multiplier: float
    y_multiplier: float
    x_scalar_to_add: float
    y_scalar_to_add: float
    callouts: List[Callout]
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.coordinates = data.get("coordinates")
        self.display_icon = data.get("displayIcon")
        self.list_view_icon = data.get("listViewIcon")
        self.splash = data.get("splash")
        self.asset_path = data.get("assetPath")
        self.map_url = data.get("mapUrl")
        self.x_multiplier = data.get("xMultiplier")
        self.y_multiplier = data.get("yMultiplier")
        self.x_scalar_to_add = data.get("xScalarToAdd")
        self.y_scalar_to_add = data.get("yScalarToAdd")
        self.callouts = [Callout(x) for x in data.get("callouts")] if data.get("callouts") else []
        self.raw_data = data
