import uuid
from datetime import datetime, timedelta, time
from typing import Dict


def default_isoformat(obj: datetime):
    if isinstance(obj, (datetime, timedelta)):
        return obj.isoformat()


def default_utc(obj: datetime):
    if isinstance(obj, (datetime, timedelta)):
        return obj.utcnow()


class Payload:
    def __init__(self, payload: Dict):
        self.payload = payload

    @classmethod
    def new_payload(cls, user_id, duration: timedelta):
        token_id = str(uuid.uuid4())
        payload: Dict = {
            "jti": token_id,
            "sub": user_id,
            "iat": default_utc(datetime.now()),
            "exp": default_utc(datetime.now().__add__(duration))
        }
        return cls(payload)
