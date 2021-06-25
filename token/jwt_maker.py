from maker import Maker
import jwt
from payload import Payload
from TokenExceptions import InvalidKeySizeException, ErrInvalidTokenException, ErrExpiredTokenException

MINIMUM_SECRET_KEY_SIZE = 32


class JWTMaker(Maker):
    def __init__(self, secret_key: bytes):
        self.secret_key = secret_key

    @classmethod
    def new_jwt_maker(cls, secret_key):
        if len(secret_key) < MINIMUM_SECRET_KEY_SIZE:
            raise InvalidKeySizeException(f"invalid token size required {MINIMUM_SECRET_KEY_SIZE}")
        return cls(secret_key)

    def create_token(self, user_id, duration):
        payload = Payload.new_payload(user_id, duration)
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm="HS256"
        )

    def verify_token(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return ErrExpiredTokenException("invalid token expired")
        except jwt.InvalidTokenError:
            return ErrInvalidTokenException('invalid token provided')
