import logging
import traceback
import sys
sys.path.append('.')
sys.path.append('./src/infra')

import psycopg2

from config import ProductionConfig
from helper import Singleton

logger = logging.getLogger(__name__)


class PostgreSqlServerConnection(metaclass=Singleton):
    def __init__(self, config=ProductionConfig):
        self.server = config.server
        self.port = config.port
        self.database = config.database
        self.username = config.username
        self.password = config.password
        self._connect()
    
    def _connect(self):
        self.conn = psycopg2.connect(dbname=self.database, user=self.username,
                                     password=self.password, host=self.server, port=self.port)


    def __enter__(self):
        logger.debug('Iniciando conexao com o Banco de Dados Stonelog',
                     extra={'server': self.server,
                            'port': self.port,
                            'database': self.database,
                            'username': self.username})
        if not self.conn or self.conn.closed:
            self._connect()
        
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
