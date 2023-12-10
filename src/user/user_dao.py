import sys
sys.path.append('./src/infra')

from user import User
from pgsql_connection import PostgreSqlServerConnection


class UserDao:
    @staticmethod
    def create(user: User) -> User:
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
    def get_by_email(email: str) -> User:
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
    def get_by_id(id: int) -> User:
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
    def update(user: User) -> User:
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
    def delete(user: User) -> User:
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