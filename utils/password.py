import bcrypt
from functools import wraps


def _encode_password(func):
    @wraps(func)
    def bcrypt_encoder(password: str, *args, **kwargs):
        if password:
            salt = bcrypt.gensalt()
            hash_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
            return func(hash_pw, *args, **kwargs)
        return bcrypt_encoder


@_encode_password
def hash_password(password):
    return password


def check_password(password, hash_passwd) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hash_passwd)
