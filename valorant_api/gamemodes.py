from typing import List, Union


class GameFeatureOverride:
    feature_name: str
    state: bool

    def __init__(self, data: dict) -> None:
        self.feature_name = data.get("featureName")
        self.state = data.get("state")


class GameMode:
    uuid: str
    display_name: str
    duration: Union[str, None]
    is_team_voice_allowed: bool
    is_minimap_hidden: bool
    orb_count: int
    team_roles: Union[List[str], None]
    game_feature_overrides: Union[List[GameFeatureOverride], None]
    display_icon: Union[str, None]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.duration = data.get("duration")
        self.is_team_voice_allowed = data.get("isTeamVoiceAllowed")
        self.is_minimap_hidden = data.get("isMinimapHidden")
        self.orb_count = data.get("orbCount")
        self.team_roles = data.get("teamRoles")
        self.game_feature_overrides = data.get("gameFeatureOverrides")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data

class Equippable:
    uuid: str
    display_name: str
    category: str
    display_icon: str
    kill_stream_icon: str
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict):
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.category = data.get("category")
        self.display_icon = data.get("displayIcon")
        self.kill_stream_icon = data.get("killStreamIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data
