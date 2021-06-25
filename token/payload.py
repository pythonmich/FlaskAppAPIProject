import datetime
import uuid


def default(obj):
    if isinstance(obj, (datetime.datetime, datetime.timedelta)):
        return obj.isoformat()


class Payload:
    def __init__(self, payload: dict):
        self.payload = payload

    @classmethod
    def new_payload(cls, user_id, duration):
        token_id = str(uuid.uuid4())
        payload = {
            "id": token_id,
            "sub": user_id,
            "iat": default(datetime.datetime.now()),
            "exp": default(datetime.datetime.now().__add__(duration))
        }
        return cls(payload)
