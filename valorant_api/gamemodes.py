from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GameFeatureOverride:
    feature_name: str
    state: bool

    def __init__(self, data: dict) -> None:
        self.feature_name = data.get("featureName")
        self.state = data.get("state")


@dataclass
class GameRuleBoolOverride:
    rule_name: str
    state: bool

    def __init__(self, data: dict) -> None:
        self.rule_name = data.get("ruleName")
        self.state = data.get("state")


@dataclass
class GameMode:
    uuid: str
    display_name: Optional[str]
    duration: Optional[str]
    allows_match_timeouts: bool
    is_team_voice_allowed: bool
    is_minimap_hidden: bool
    orb_count: int
    team_roles: Optional[List[str]]
    game_feature_overrides: Optional[List[GameFeatureOverride]]
    game_rule_bool_overrides: Optional[List[GameRuleBoolOverride]]
    display_icon: Optional[str]
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.duration = data.get("duration")
        self.a = data.get("allowsMatchTimeouts")
        self.is_team_voice_allowed = data.get("isTeamVoiceAllowed")
        self.is_minimap_hidden = data.get("isMinimapHidden")
        self.orb_count = data.get("orbCount")
        self.team_roles = data.get("teamRoles")
        self.game_feature_overrides = data.get("gameFeatureOverrides")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data


@dataclass
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
