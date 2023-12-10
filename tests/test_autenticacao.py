import unittest
from src.user.user import User
from src.user.user_dao import create


class TestUsuarioAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        a = create(user, token="Teste")
        self.assertIsNotNone(a)

class TestUsuarioNaoAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        # Supondo que 'token' seja um argumento esperado pela função decorada.
        self.assertRaises(ValueError, create, user, token="NaoAutenticado")


