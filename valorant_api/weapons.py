from dataclasses import dataclass
from typing import Optional, List


@dataclass
class GridPosition:
    row: int
    column: int

    def __init__(self, data: dict) -> None:
        self.row = data.get("row")
        self.column = data.get("column")


@dataclass
class ShopData:
    cost: int
    category: str
    category_text: str
    grid_position: Optional[GridPosition]
    image: str
    new_image: str
    new_image2: str
    asset_path: str

    def __init__(self, data: dict):
        self.cost = data.get("cost")
        self.category = data.get("category")
        self.category_text = data.get("categoryText")
        self.grid_position = GridPosition(data.get("gridPosition")) if data.get("gridPosition") is not None else None
        self.image = data.get("image")
        self.new_image = data.get("newImage")
        self.new_image2 = data.get("newImage2")
        self.asset_path = data.get("assetPath")


@dataclass
class Chroma:
    uuid: str
    display_name: str
    display_icon: str
    full_render: str
    swatch: Optional[str]
    streamed_video: Optional[str]
    asset_path: str

    def __init__(self, data: dict):
        self.raw_data = data
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.display_icon = data.get("displayIcon")
        self.full_render = data.get("fullRender")
        self.swatch = data.get("swatch")
        self.streamed_video = data.get("streamedVideo")
        self.asset_path = data.get("assetPath")


@dataclass
class Level:
    uuid: str
    display_name: str
    level_item: Optional[str]
    display_icon: str
    streamed_video: Optional[str]
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.raw_data = data
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.level_item = data.get("levelItem")
        self.display_icon = data.get("displayIcon")
        self.streamed_video = data.get("streamedVideo")
        self.asset_path = data.get("assetPath")


@dataclass
class Skin:
    uuid: str
    display_name: str
    theme_uuid: str
    content_tier_uuid: Optional[str]
    wallpaper: Optional[str]
    display_icon: str
    asset_path: str
    chromas: List[Optional[Chroma]]
    levels: List[Optional[Level]]

    def __init__(self, data: dict):
        self.raw_data = data
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.theme_uuid = data.get("themeUuid")
        self.content_tier_uuid = data.get("contentTierUuid")
        self.wallpaper = data.get("wallpaper")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.chromas = [Chroma(x) for x in data.get("chromas") if x is not None]
        self.levels = [Level(x) for x in data.get("levels") if x is not None]


@dataclass
class AdsStats:
    zoom_multiplier: float
    fire_rate: float
    run_speed_multiplier: float
    burst_count: int
    first_bullet_accuracy: float

    def __init__(self, data: dict):
        self.zoom_multiplier = data.get("zoomMultiplier")
        self.fire_rate = data.get("fireRate")
        self.run_speed_multiplier = data.get("runSpeedMultiplier")
        self.burst_count = data.get("burstCount")
        self.first_bullet_accuracy = data.get("firstBulletAccuracy")


@dataclass
class DamageRange:
    range_start_meters: int
    range_end_meters: int
    head_damage: float
    body_damage: int
    leg_damage: float

    def __init__(self, data: dict) -> None:
        self.range_start_meters = data.get("rangeStartMeters")
        self.range_end_meters = data.get("rangeEndMeters")
        self.head_damage = data.get("headDamage")
        self.body_damage = data.get("bodyDamage")
        self.leg_damage = data.get("legDamage")


@dataclass
class AirBurstStats:
    shotgun_pellet_count: int
    burst_distance: float

    def __init__(self, data: dict):
        self.shotgun_pellet_count = data.get("shotgunPelletCount")
        self.burst_distance = data.get("burstDistance")


@dataclass
class AltShotgunStats:
    shotgun_pellet_count: int
    burst_rate: float

    def __init__(self, data: dict) -> None:
        self.shotgun_pellet_count = data.get("shotgunPelletCount")
        self.burst_rate = data.get("burstRate")


@dataclass
class WeaponStats:
    fire_rate: int
    magazine_size: int
    run_speed_multiplier: float
    equip_time_seconds: float
    reload_time_seconds: int
    first_bullet_accuracy: float
    shotgun_pellet_count: int
    wall_penetration: str
    feature: str
    fire_mode: Optional[str]
    alt_fire_type: str
    ads_stats: Optional[AdsStats]
    alt_shotgun_stats: AltShotgunStats
    air_burst_stats: AirBurstStats
    damage_ranges: List[DamageRange]

    def __init__(self, data: dict) -> None:
        self.fire_rate = data.get("fireRate")
        self.magazine_size = data.get("magazineSize")
        self.run_speed_multiplier = data.get("runSpeedMultiplier")
        self.equip_time_seconds = data.get("equipTimeSeconds")
        self.reload_time_seconds = data.get("reloadTimeSeconds")
        self.first_bullet_accuracy = data.get("firstBulletAccuracy")
        self.shotgun_pellet_count = data.get("shotgunPelletCount")
        self.wall_penetration = data.get("wallPenetration")
        self.feature = data.get("feature")
        self.fire_mode = data.get("fireMode")
        self.alt_fire_type = data.get("altFireType")
        self.ads_stats = AdsStats(data.get("adsStats")) if data.get("adsStats") is not None else None
        self.alt_shotgun_stats = data.get("altShotgunStats")
        self.air_burst_stats = data.get("airBurstStats")
        self.damage_ranges = [DamageRange(x) for x in data.get("damageRanges")]


@dataclass
class Weapon:
    uuid: str
    display_name: str
    category: str
    default_skin_uuid: str
    display_icon: str
    kill_stream_icon: str
    asset_path: str
    weapon_stats: Optional[WeaponStats]
    shop_data: Optional[ShopData]
    skins: Optional[List[Skin]]
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.category = data.get("category")
        self.default_skin_uuid = data.get("defaultSkinUuid")
        self.display_icon = data.get("displayIcon")
        self.kill_stream_icon = data.get("killStreamIcon")
        self.asset_path = data.get("assetPath")
        self.weapon_stats = WeaponStats(data.get("weaponStats")) if data.get("weaponStats") is not None else None
        self.shop_data = ShopData(data.get("shopData")) if data.get("shopData") is not None else None
        self.skins = [Skin(x) for x in data.get("skins")] if data.get("skins") is not None else None
        self.raw_data = data
