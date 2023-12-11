import base64
import os

from dotenv import load_dotenv
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

load_dotenv()
SECRET = os.getenv('SECRET').encode()


class User:
    def __init__(self, name: str, email: str, password: str, token: str, last_name: str, level: str = None, id: int = None, is_password_hashed: bool = False):
        """
        Initialize the User object
        self.name: user name
        self.email: user email address
        self.password: user password
        self.token: user token used to authenticate the user
        self.last_name: user last name
        self.level: user seniority level
        self._id: user id used to identify the user in the database
        """
        self.name = name
        self.email = email
        if is_password_hashed:
            self.password = password
        else:
            self.password = User.generate_key(password)
        self.token = token
        self.last_name = last_name
        if level is None:
            self.level = 'Sem experiência'
        else:
            self.level = level
        self._id = id
    
    def check_password(self, password: str) -> bool:
        """
        Check if the provided password is correct
        Args:
            password(str): password to be checked
        Returns:
            True if the provided password is correct, False otherwise
        """
        return self.password == User.generate_key(password)
    
    @staticmethod
    def generate_key(password: str, secret: bytes = SECRET) -> str:
        """
        Generate a key from a password
        Args:
            password(str): password used to generate the key
            secret(bytes): secret used to generate the key
        Returns:
            key
        """
        kdf = PBKDF2HMAC(algorithm=hashes.SHA3_512(), length=32, salt=secret, iterations=100000, backend=default_backend())
        return str(base64.urlsafe_b64encode(kdf.derive(password.encode())))