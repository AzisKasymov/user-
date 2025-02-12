import unittest
from user import User
from userservice import UserService
from userutil import UserUtil
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("abduazis", "kasymov", datetime(2006, 8, 5))
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

            def test_get_number(self):
                UserService.users.clear()
                user1 = User("Charlie", "Davis", datetime(2001, 12, 5))
                user2 = User("Diana", "Evans", datetime(1999, 8, 23))
                UserService.add_user(user1)
                UserService.add_user(user2)
                self.assertEqual(UserService.get_number(), 2)

    class TestUserUtil(unittest.TestCase):
            def test_generate_user_id(self):
                user_id = UserUtil.generate_user_id()
                self.assertTrue(str(user_id).startswith(str(datetime.today().year)[-2:]))
                self.assertEqual(len(str(user_id)), 9)

            def test_generate_password(self):
                password = UserUtil.generate_password()
                self.assertTrue(UserUtil.is_strong_password(password))

            def test_validate_email(self):
                self.assertTrue(UserUtil.validate_email("azisomon@gmail.com"))
                self.assertFalse(UserUtil.validate_email("aziskas@gmail.com"))
