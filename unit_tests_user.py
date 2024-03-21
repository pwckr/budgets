import unittest
from io import StringIO
import sys

# Import the class UserManager here
from usermanagement import UserManager

class TestUserManager(unittest.TestCase):
    """Unit Test Class for UserManager."""

    def setUp(self):
        self.user_manager = UserManager()
        self.user_manager.users = {"user1", "user2", "user3"}
        self.user_manager.budgets = {}
        self.user_manager.spendings = {}


    def test_retrieve_username(self):
        user_input = StringIO('test_user\n')
        sys.stdin = user_input
        username = self.user_manager.retrieve_username()
        self.assertEqual(username, 'test_user')


    def test_check_for_account_existing(self):
        result = self.user_manager.check_for_account("user1")
        self.assertTrue(result)


    def test_check_for_account_non_existing(self):
        result = self.user_manager.check_for_account("non_existing_user")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
