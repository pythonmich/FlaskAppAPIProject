from abc import ABC, abstractmethod


class Maker(ABC):
    @abstractmethod
    def create_token(self, user_id, duration):
        """create token"""

    @abstractmethod
    def verify_token(self, token):
        """verifies the token"""
