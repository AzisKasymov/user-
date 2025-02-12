import unittest
from user import User
from userservice import UserService
from userutil import UserUtil
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("John", "Doe", datetime(2000, 5, 20))
        self.assertEqual(user.name, "John")
        self.assertEqual(user.surname, "Doe")
        self.assertTrue(UserUtil.validate_email(user.email))
        self.assertTrue(UserUtil.is_strong_password(user.password))