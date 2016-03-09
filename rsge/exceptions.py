class RsError(Exception):
    pass


class RsApiError(RsError):
    def __init__(self, msg, error_code, *args, **kwargs):
        self.msg = msg
        self.error_code = int(error_code)
        super(RsError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "RsApiError %d: %s" % (self.error_code, self.msg)


class RsAuthorizationError(RsError):
    pass
