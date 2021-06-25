class BaseTokenExceptions(Exception):
    pass


class ErrInvalidTokenException(BaseTokenExceptions):
    def __init__(self, err_str):
        self.err_str = err_str


class ErrExpiredTokenException(BaseTokenExceptions):
    def __init__(self, err_str):
        self.err_str = err_str


class InvalidKeySizeException(BaseTokenExceptions):
    def __init__(self, err_str):
        self.err_str = err_str
