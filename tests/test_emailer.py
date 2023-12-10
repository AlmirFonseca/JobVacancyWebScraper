import unittest
from src.emailer.emailer import Emailer


class TestEmailer(unittest.TestCase):
    def test_is_valid_email_with_email(self):
        email = "teste@gmail.com"
        self.assertTrue(Emailer.is_valid_email(email))

    def test_is_valid_email_no_dot_email(self):
        email = "teste@gmailcom"
        self.assertFalse(Emailer.is_valid_email(email))

    def test_is_valid_email_no_at_sign_email(self):
        email = "testegmail.com"
        self.assertFalse(Emailer.is_valid_email(email))

    def test_is_valid_email_with_plus_number(self):
        email = "teste+1@gmail.com"
        self.assertTrue(Emailer.is_valid_email(email))

    def test_is_valid_email_with_underline(self):
        email = "teste_t@gmail.com"
        self.assertTrue(Emailer.is_valid_email(email))


if __name__ == '__main__':
    unittest.main()
