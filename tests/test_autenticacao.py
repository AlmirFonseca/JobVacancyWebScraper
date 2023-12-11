import unittest
import sys
sys.path.append('./src/models')
sys.path.append('./src/daos')
from user import User
from user_dao import create, get_by_email


class TestUsuarioAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        a = create(user, token="Teste")
        self.assertIsNotNone(a)

class TestUsuarioNaoAutenticado(unittest.TestCase):
    def test_is_connected(self):
        user = User('João', 'a', '123', '123', 'Silva')
        # Supondo que 'token' seja um argumento esperado pela função decorada.
        self.assertRaises(ValueError, get_by_email, 'a', token="NaoAutenticado")

if __name__ == '__main__':
    unittest.main()