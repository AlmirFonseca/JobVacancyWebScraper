import sys
sys.path.append('./src/infra')

from pgsql_connection import PostgreSqlServerConnection

def valida_autenticacao(f):
    def wrapper(*args, **kargs):
        token=kargs.get('token')
        if not token:
            raise ValueError("Usuário não autenticado")
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT user_id FROM users WHERE user_token = %s', (token,))
                row = cursor.fetchone()
                if not row:
                    raise ValueError("Usuário não autenticado")
        return f(*args, **kargs)

    return wrapper