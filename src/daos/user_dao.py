from .database_facade import update as db_update, insert, select, delete as db_delete
import sys
sys.path.append('./src')
sys.path.append('./src/models')

from user import User
from helper import valida_autenticacao


def create(user: User, *args, **kargs) -> User:
    """
    Create a new user in the database
    Args:
        user(User): User object
    Returns:
        User created
    """
    data = {
        'user_name': user.name,
        'user_email': user.email,
        'user_password': user.password,
        'user_token': user.token,
        'user_last_name': user.last_name,
        'user_level': user.level
    }
    id = insert('users', data, ('user_id',))[0]
    user._id = id
    return user

@valida_autenticacao
def get_by_email(email: str, *args, **kargs) -> User:
    """
    Get a user by email
    Args:
        email(str): user email address
    Returns:
        User object
    """
    table = 'users'
    columns = ('user_name', 'user_email', 'user_password', 'user_token', 'user_last_name', 'user_level', 'user_id')
    where = {'user_email': email}
    fetch = select(table, columns, where)
    return User(*fetch[0]) if fetch else None

@valida_autenticacao
def get_by_id(id: int, *args, **kargs) -> User:
    """
    Get a user by id
    Args:
        id(int): user id
    Returns:
        User object
    """
    table = 'users'
    columns = ('user_name', 'user_email', 'user_password', 'user_token', 'user_last_name', 'user_level', 'user_id')
    where = {'user_id': id}
    fetch = select(table, columns, where)
    return User(*fetch[0]) if fetch else None

@valida_autenticacao
def update(user: User, *args, **kargs) -> bool:
    """
    Update a user in the database
    Args:
        user(User): User object
    Returns:
        bool: True if user was updated, False otherwise
    """
    data = {
        'user_name': user.name,
        'user_email': user.email,
        'user_password': user.password,
        'user_token': user.token,
        'user_last_name': user.last_name,
        'user_level': user.level
    }
    where = {'user_id': user._id}
    return db_update('users', data, where)

@valida_autenticacao
def delete(id: int, *args, **kargs) -> bool:
    """
    Delete a user in the database
    Args:
        id(int): user id
    Returns:
        bool: True if user was deleted, False otherwise
    """
    where = {'user_id': id}
    return db_delete('users', where)