from dataclasses import dataclass
from typing import Optional
from .utils import Mapper


@dataclass
class GridPosition(Mapper):
    row: Optional[int] = None
    column: Optional[int] = None

    def __init__(self):
        super().__init__()

@dataclass
class ShopData(Mapper):
    cost: Optional[int] = None
    category: Optional[str] = None
    category_text: Optional[str] = None
    grid_position: Optional[GridPosition] = None
    can_be_trashed: Optional[bool] = None
    image: Optional[str] = None
    new_image: Optional[str] = None
    new_image2: Optional[str] = None
    asset_path: Optional[str] = None

    def __init__(self):
        super().__init__()

@dataclass
class Gear(Mapper):
    uuid: str
    raw_data: dict
    display_name: Optional[str] = None
    description: Optional[str] = None
    display_icon: Optional[str] = None
    asset_path: Optional[str] = None
    shop_data: Optional[ShopData] = None

    def __init__(self, data: dict):
        self.raw_data = data
        self.map(childclasses={"shopData": ShopData, "gridPosition": GridPosition})
