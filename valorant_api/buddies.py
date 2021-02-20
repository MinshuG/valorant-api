class Buddy:
    uuid: str
    display_name: str
    is_hidden_if_not_owned: bool
    theme_uuid: None
    display_icon: str
    asset_path: str
    raw_data: dict

    def __init__(self, data: dict):
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.is_hidden_if_not_owned = data.get("isHiddenIfNotOwned")
        self.theme_uuid = data.get("themeUuid")
        self.display_icon = data.get("displayIcon")
        self.asset_path = data.get("assetPath")
        self.raw_data = data

    def __str__(self):
        return str(self.raw_data)
