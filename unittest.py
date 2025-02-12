import unittest
from user import User
from userservice import UserService
from userutil import UserUtil
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("abduazis", "kasymov", datetime(2006, 8, 05))
        self.assertEqual(user.name, "abduazis")
        self.assertEqual(user.surname, "kasymov")
        self.assertTrue(UserUtil.validate_email(user.email))
        self.assertTrue(UserUtil.is_strong_password(user.password))

        def test_get_age(self):
            user = User("azis", "asan", datetime(1995, 3, 15))
            self.assertEqual(user.get_age(), datetime.today().year - 1995)

    class TestUserService(unittest.TestCase):
        def test_add_find_delete_user(self):
            user = User("Bob", "Brown", datetime(1998, 7, 10))
            UserService.add_user(user)
            self.assertEqual(UserService.find_user(user.user_id), user)
            self.assertTrue(UserService.delete_user(user.user_id))
            self.assertIsNone(UserService.find_user(user.user_id))