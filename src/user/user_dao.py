import sys
sys.path.append('./src/infra')

from src.user.user import User
from src.helper import valida_autenticacao
from src.infra.pgsql_connection import PostgreSqlServerConnection


class UserDao:
    @staticmethod
    @valida_autenticacao
    def create(user: User, *args, **kargs) -> User:
        """
        Create a new user in the database
        Args:
            user(User): User object
        Returns:
            User object
        """
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO users (user_name, user_email, user_password, user_token, user_last_name, user_level) VALUES (%s, %s, %s, %s, %s, %s) RETURNING user_id', (user.name, user.email, user.password, user.token, user.last_name, user.level))
                user_id = cursor.fetchone()[0]
                conn.commit()
                user._id = user_id
                return user

    @staticmethod
    @valida_autenticacao
    def get_by_email(email: str, *args, **kargs) -> User:
        """
        Get a user by email
        Args:
            email(str): user email address
        Returns:
            User object
        """
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT user_name, user_email, user_password, user_token, user_last_name, user_level, user_id FROM users WHERE user_email = %s', (email,))
                row = cursor.fetchone()
                if row:
                    return User(*row)
                return None

    @staticmethod
    @valida_autenticacao
    def get_by_id(id: int, *args, **kargs) -> User:
        """
        Get a user by id
        Args:
            id(int): user id
        Returns:
            User object
        """
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT user_name, user_email, user_password, user_token, user_last_name, user_level, user_id FROM users WHERE user_id = %s', (id,))
                row = cursor.fetchone()
                if row:
                    return User(*row)
                return None

    @staticmethod
    @valida_autenticacao
    def update(user: User, *args, **kargs) -> User:
        """
        Update a user in the database
        Args:
            user(User): User object
        Returns:
            User object
        """
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('UPDATE users SET name = %s, email = %s, password = %s, token = %s, last_name = %s, level = %s WHERE id = %s', (user.name, user.email, user.password, user.token, user.last_name, user.level, user._id))
                conn.commit()
                return user
    
    @staticmethod
    @valida_autenticacao
    def delete(user: User, *args, **kargs) -> User:
        """
        Delete a user in the database
        Args:
            user(User): User object
        Returns:
            User object
        """
        with PostgreSqlServerConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM users WHERE id = %s', (user._id,))
                conn.commit()
                return user