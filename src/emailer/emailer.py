import re
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText


class Emailer:
    def __init__(self):
        load_dotenv()
        self.address = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.smtp_servers = {
            'gmail.com': ('smtp.gmail.com', 587),
            'outlook.com': ('smtp-mail.outlook.com', 587),
            'hotmail.com': ('smtp-mail.outlook.com', 587),
            'yahoo.com': ('smtp.mail.yahoo.com', 587),
            'gmx.com': ('mail.gmx.com', 587),
            'fgv.edu.br': ('smtp-mail.outlook.com', 587)
        }

    def _start_server(self, username: str) -> smtplib.SMTP:
        if not self.is_valid_email(username):
            raise ValueError(f'{username} is not a valid email address')
        domain = username.split('@')[1]
        smtp_server = self.smtp_servers.get(domain)[0]
        smtp_portnumber = self.smtp_servers.get(domain)[1]
        if smtp_server is None:
            raise ValueError(f'SMTP server not found for domain {domain}')
        return smtplib.SMTP(smtp_server, smtp_portnumber)
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
                Checks if the provided email address is valid
                Args:
                    email(str): The email address
                Returns:
                    True if the provided email address is valid, False otherwise
                """
        # compilation error
        # email_regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        # doesn't pass test_is_valid_email_with_plus_number
        # email_regex = r'^[a-zA-Z0-9-.]+@([\w-]+\.)+[\w-]{2,4}$'
        email_regex = r'^[a-zA-Z0-9_.+-]+@([\w-]+\.)+[\w-]{2,4}$'

        return bool(re.match(email_regex, email))

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        if not self.is_valid_email(to_email):
            raise ValueError(f'{to_email} is not a valid email address')

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = self.address
        message['To'] = to_email

        with self._start_server(self.address) as server:
            server.starttls()
            server.login(user=self.address, password=self.password)
            server.send_message(message)
