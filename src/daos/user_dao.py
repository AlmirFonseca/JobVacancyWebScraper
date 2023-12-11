import database_facade as dbf
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
    id = dbf.insert('users', data, ('user_id',))[0]
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
    fetch = dbf.select(table, columns, where)
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
    fetch = dbf.select(table, columns, where)
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
    return dbf.update('users', data, where)

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
    return dbf.delete('users', where)