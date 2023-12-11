import unittest
import sys
sys.path.append('./src/infra')
from pgsql_connection import PostgreSqlServerConnection


class TestDBConnection(unittest.TestCase):
    def test_is_connected(self):
        conn = PostgreSqlServerConnection()
        self.assertTrue(conn.conn)
    
    def test_is_singleton(self):
        conn1 = PostgreSqlServerConnection()
        conn2 = PostgreSqlServerConnection()
        self.assertEqual(conn1, conn2)
    
    def test_is_connected_with_context_manager(self):
        with PostgreSqlServerConnection() as conn:
            self.assertTrue(conn)
    
    def test_is_connected_with_context_manager_and_cursor(self):
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                self.assertTrue(cursor)
    
    def test_run_query(self):
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('select 1;')
                result = cursor.fetchall()
                self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
