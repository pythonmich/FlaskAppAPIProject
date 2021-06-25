from datetime import datetime
import uuid

from api.server import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import VARCHAR, DateTime
import pytz
from utils.password import hash_password


class User(db.Model):
    # TODO: CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    __tablename__ = "users"
    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4())
    username = db.Column(VARCHAR(70), nullable=False, unique=True)
    hash_password = db.Column(VARCHAR(80), nullable=False)
    email = db.Column(VARCHAR(150), unique=True, nullable=False)
    password_changed_at = db.Column(DateTime(timezone=True), nullable=False, default="0001-01-01 00:00:00Z")
    created_at = db.Column(DateTime(timezone=True), nullable=False,
                           default=datetime.now(tz=pytz.timezone("Africa/Nairobi")))
    deleted_at = db.Column(DateTime(timezone=True), nullable=False, default="0001-01-01 00:00:00Z")

    def __init__(self, username, password, email):
        self.email = email
        self.password: str = hash_password(password).decode('utf-8')
        self.username = username
