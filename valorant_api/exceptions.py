class ValorantApi(Exception):
    pass


class InvalidOrMissingParameter(ValorantApi):  # 400
    pass


class NotFound(ValorantApi):  # 404
    pass

class AttributeExistsError(ValorantApi):
    pass
