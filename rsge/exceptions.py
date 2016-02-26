class RsError(Exception):
    pass


class RsApiError(RsError):
    pass


class RsAuthorizationError(RsError):
    pass
