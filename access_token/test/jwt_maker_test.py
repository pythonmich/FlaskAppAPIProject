import time
import unittest
import uuid
from datetime import timedelta

import jwt

from access_token.jwt_maker import JWTMaker, ErrExpiredTokenMSG, ErrInvalidTokenMSG
from access_token.payload import Payload
from utils.randoms import random_string


class JWTMakerTest(unittest.TestCase):
    def test_jwt_maker(self):
        maker = JWTMaker.new_jwt_maker(random_string(32).encode("utf-8"))
        user_id = str(uuid.uuid4())
        duration = timedelta(minutes=1)

        token = maker.create_token(user_id, duration)
        self.assertNotEqual(token, "")

        payload = maker.verify_token(token)
        self.assertIsNotNone(payload)

        self.assertTrue(payload["jti"] != 0)
        self.assertEqual(payload["sub"], user_id)

    def test_expired_token(self):
        maker = JWTMaker.new_jwt_maker(random_string(32).encode("utf-8"))
        user_id = str(uuid.uuid4())
        duration = timedelta(microseconds=1)
        token = maker.create_token(user_id, duration)
        self.assertNotEqual(token, "")
        time.sleep(1)
        expired = maker.verify_token(token)
        self.assertEqual(expired, ErrExpiredTokenMSG)

    def test_invalid_token(self):
        maker = JWTMaker.new_jwt_maker(random_string(32).encode("utf-8"))
        token = ""
        invalid = maker.verify_token(token)
        self.assertEqual(invalid, ErrInvalidTokenMSG)

    def test_none_algorithm(self):
        maker = JWTMaker.new_jwt_maker(random_string(32).encode("utf-8"))
        payload = Payload.new_payload(random_string(10), timedelta(minutes=1))
        with self.assertRaises(jwt.InvalidKeyError):
            jwt.encode(
                vars(payload).get("payload"),
                maker.secret_key,
                algorithm=None
            )


if __name__ == '__main__':
    unittest.main()
