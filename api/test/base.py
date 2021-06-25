from flask_testing import TestCase
from api.server import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("api.app_config.DevelopmentConfig")
        return app

    def setUp(self) -> None:
        db.create_all()
        db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()