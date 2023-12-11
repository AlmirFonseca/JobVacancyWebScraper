import unittest
from src.models.user import User
from src.daos.user_dao import update


class TestUsuarioAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        a = update(user, token="Teste")
        self.assertIsNotNone(a)

class TestUsuarioNaoAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        # Supondo que 'token' seja um argumento esperado pela função decorada.
        self.assertRaises(ValueError, update, user, token="NaoAutenticado")


