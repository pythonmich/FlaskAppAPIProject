class BaseTokenExceptions(Exception):
    pass

class InvalidKeySizeException(BaseTokenExceptions):
    def __init__(self, err_str):
        self.err_str = err_str
