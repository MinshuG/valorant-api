class PlayerCard:
    uuid: str
    display_name: str
    is_hidden_if_not_owned: bool
    display_icon: str
    small_art: str
    wide_art: str
    large_art: str
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.is_hidden_if_not_owned = data.get("isHiddenIfNotOwned")
        self.display_icon = data.get("displayIcon")
        self.small_art = data.get("smallArt")
        self.wide_art = data.get("wideArt")
        self.large_art = data.get("largeArt")
        self.asset_path = data.get("assetPath")
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
