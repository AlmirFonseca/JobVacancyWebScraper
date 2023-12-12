import unittest
import sys
sys.path.append('./src/emailer')
from emailer import Emailer
from email.mime.text import MIMEText
from unittest.mock import patch


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

    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        emailer = Emailer()

        emailer.send_email('job.web.scraper@gmx.com', 'Subject', 'Message')

        # check if SMTP was called with the correct server and port
        mock_smtp.assert_called_with('mail.gmx.com', 587)

        # get the mock SMTP instance
        instance = mock_smtp.return_value

        # check if the login, sendmail, and quit methods were called with the correct arguments
        instance.__enter__().login.assert_called_with(user=emailer.address, password=emailer.password)
        instance.__exit__.assert_called_once()

        # get the arguments that send_message was called with
        send_message_args = instance.__enter__().send_message.call_args[0]

        # check the content of the MIMEText object
        self.assertEqual(send_message_args[0].get_payload(), 'Message')
        self.assertEqual(send_message_args[0]['Subject'], 'Subject')
        self.assertEqual(send_message_args[0]['From'], emailer.address)
        self.assertEqual(send_message_args[0]['To'], 'job.web.scraper@gmx.com')

    def test_emailer_is_singleton(self):
        emailer = Emailer()
        emailer2 = Emailer()
        self.assertIs(emailer, emailer2)


if __name__ == '__main__':
    unittest.main()
