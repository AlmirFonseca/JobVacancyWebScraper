import unittest
import sys
sys.path.append('./src/models')

from user import User
from daos.user_dao import *


class TestUser(unittest.TestCase):
    def test_same_password_generates_same_key(self):
        key1 = User.generate_key('password')
        key2 = User.generate_key('password')
        self.assertEqual(key1, key2)
    
    def test_diffent_passwords_generate_different_keys(self):
        key1 = User.generate_key('password1')
        key2 = User.generate_key('password2')
        self.assertNotEqual(key1, key2)
    
    def test_crud_user(self):
        user_test = User('Sheldon', 'sheldon@gmail.com', 'password', 'token', 'Cooper', 1)
        user_created = create(user_test)
        test_email = get_by_email(user_test.email, token=user_test.token)
        self.assertEqual(test_email.email, user_test.email)
        test_id = get_by_id(user_created._id, token=user_test.token)
        self.assertEqual(user_test.email, test_id.email)
        user_deleted = delete(user_created._id, token=user_test.token)
        self.assertIsNotNone(user_deleted)


if __name__ == '__main__':
    unittest.main()