import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app_settings = os.getenv(
    "APP_SETTINGS",
    "api.app_config.DevelopmentConfig"
)
app.config.from_object(app_settings)
db = SQLAlchemy(app)