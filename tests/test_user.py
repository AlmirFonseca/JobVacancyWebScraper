import unittest
import sys
sys.path.append('./src/user')

from user import User


class TestUser(unittest.TestCase):
    def test_same_password_generates_same_key(self):
        key1 = User.generate_key('password')
        key2 = User.generate_key('password')
        self.assertEqual(key1, key2)
    
    def test_diffent_passwords_generate_different_keys(self):
        key1 = User.generate_key('password1')
        key2 = User.generate_key('password2')
        self.assertNotEqual(key1, key2)


if __name__ == '__main__':
    unittest.main()