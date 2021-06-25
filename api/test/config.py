import unittest

from flask_testing import TestCase
from api.server import app
from flask import current_app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("api.app_config.DevelopmentConfig")
        return app

    def test_app_development(self):
        self.assertIsNotNone(app.config["SECRET_KEY"])
        self.assertFalse(app.config["SECRET_KEY"] == "My Secret Key")
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config[
                "SQLALCHEMY_DATABASE_URI"] == "postgresql://python_mich:Musyimi7.@localhost:5432/flask_app?sslmode=disable"
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("api.app_config.ProductionConfig")
        return app

    def test_app_production(self):
        self.assertTrue(app.config["DEBUG"] is False)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("api.app_config.TestingConfig")
        return app

    def test_app_testing(self):
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertTrue(app.config["TESTING"] is True)
        self.assertTrue(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] is False)
        self.assertTrue(
            app.config[
                "SQLALCHEMY_DATABASE_URI"] == "postgresql://python_mich:Musyimi7.@localhost:5432/flask_app_test?sslmode=disable"
        )


if __name__ == '__main__':
    unittest.main()
