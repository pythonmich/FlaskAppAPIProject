import jwt

from access_token.TokenExceptions import InvalidKeySizeException
from access_token.maker import Maker
from access_token.payload import Payload

MINIMUM_SECRET_KEY_SIZE = 32
ErrExpiredTokenMSG = "invalid token expired"
ErrInvalidTokenMSG = "invalid token provided"


class JWTMaker(Maker):
    def __init__(self, secret_key: bytes):
        self.secret_key = secret_key

    @classmethod
    def new_jwt_maker(cls, secret_key: bytes):
        if len(secret_key) < MINIMUM_SECRET_KEY_SIZE:
            raise InvalidKeySizeException(f"invalid token size required {MINIMUM_SECRET_KEY_SIZE}")
        return cls(secret_key)

    def create_token(self, user_id, duration):
        payload = Payload.new_payload(user_id, duration)
        payload_dict = vars(payload)["payload"]
        return jwt.encode(
            payload_dict,
            self.secret_key,
            algorithm="HS256"
        )

    def verify_token(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return ErrExpiredTokenMSG
        except jwt.InvalidTokenError:
            return ErrInvalidTokenMSG
