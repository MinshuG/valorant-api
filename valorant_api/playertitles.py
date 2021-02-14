class PlayerTitle:
    uuid: str
    display_name: str
    isb_hidden_if_not_owned: bool
    asset_path: str

    def __init__(self, data: dict) -> None:
        self.uuid = data.get("uuid")
        self.display_name = data.get("displayName")
        self.isb_hidden_if_not_owned = data.get("isbHiddenIfNotOwned")
        self.asset_path = data.get("assetPath")
