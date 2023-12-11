import database_facade as dbf
import sys
sys.path.append('./src')

from helper import valida_autenticacao

@valida_autenticacao
def create_user_skill(user_id: int, skill_id: int, *args, **kargs) -> bool:
    """
    Creates a new user_skill in the database.
    Args:
        user_id: user id.
        skill_id: skill id.
    Returns:
        True if the user_skill was created, False otherwise.
    """
    data = {
        'user_id': user_id,
        'skill_id': skill_id,
    }
    dbf.insert('rel_user_skill', data)
    return True

@valida_autenticacao
def get_user_skills(*args, **kargs) -> list:
    """
    Gets user_skills from the database.
    Returns:
        List of tuples of user_id and skill_id.
    """
    table = 'rel_user_skill'
    columns = ('user_id', 'skill_id')
    return dbf.select(table, columns)

@valida_autenticacao
def get_user_skills_by_user_id(user_id: int, *args, **kargs) -> list:
    """
    Gets user_skills from the database by user id.
    Args:
        user_id: user id.
    Returns:
        List of tuples of user_id and skill_id.
    """
    table = 'rel_user_skill'
    columns = ('user_id', 'skill_id')
    where = {'user_id': user_id}
    return dbf.select(table, columns, where)

@valida_autenticacao
def get_user_skills_by_skill_id(skill_id: int, *args, **kargs) -> list:
    """
    Gets user_skills from the database by skill id.
    Args:
        skill_id: skill id.
    Returns:
        List of tuples of user_id and skill_id.
    """
    table = 'rel_user_skill'
    columns = ('user_id', 'skill_id')
    where = {'skill_id': skill_id}
    return dbf.select(table, columns, where)

@valida_autenticacao
def delete_user_skill(user_id: int, skill_id: int, *args, **kargs) -> bool:
    """
    Deletes a user_skill from the database.
    Args:
        user_id: user id.
        skill_id: skill id.
    """
    table = 'rel_user_skill'
    where = {
        'user_id': user_id,
        'skill_id': skill_id,
    }
    return dbf.delete(table, where)