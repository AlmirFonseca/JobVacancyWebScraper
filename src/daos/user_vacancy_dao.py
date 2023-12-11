import database_facade as dbf
import sys
sys.path.append('./src')

from helper import valida_autenticacao

@valida_autenticacao
def create_user_vacancy(user_id: int, job_id: int, *args, **kargs) -> bool:
    """
    Creates a new user_vacancy in the database.
    Args:
        user_id: user id.
        vacancy_id: vacancy id.
    Returns:
        True if the user_vacancy was created, False otherwise.
    """
    data = {
        'user_id': user_id,
        'job_id': job_id,
    }
    dbf.insert('rel_user_vacancy', data)
    return True

@valida_autenticacao
def get_user_vacancies(*args, **kargs) -> list:
    """
    Gets user_vacancies from the database.
    Returns:
        List of tuples of user_id and vacancy_id.
    """
    table = 'rel_user_vacancy'
    columns = ('user_id', 'job_id')
    return dbf.select(table, columns)

@valida_autenticacao
def get_user_vacancies_by_user_id(user_id: int, *args, **kargs) -> list:
    """
    Gets user_vacancies from the database by user id.
    Args:
        user_id: user id.
    Returns:
        List of tuples of user_id and vacancy_id.
    """
    table = 'rel_user_vacancy'
    columns = ('user_id', 'job_id')
    where = {'user_id': user_id}
    return dbf.select(table, columns, where)

@valida_autenticacao
def get_user_vacancies_by_vacancy_id(vacancy_id: int, *args, **kargs) -> list:
    """
    Gets user_vacancies from the database by vacancy id.
    Args:
        vacancy_id: vacancy id.
    Returns:
        List of tuples of user_id and vacancy_id.
    """
    table = 'rel_user_vacancy'
    columns = ('user_id', 'job_id')
    where = {'job_id': vacancy_id}
    return dbf.select(table, columns, where)

@valida_autenticacao
def delete_user_vacancy(user_id: int, job_id: int, *args, **kargs) -> bool:
    """
    Deletes a user_vacancy from the database.
    Args:
        user_id: user id.
        job_id: job id.
    Returns:
        True if the user_vacancy was deleted, False otherwise.
    """
    table = 'rel_user_vacancy'
    where = {'user_id': user_id, 'job_id': job_id}
    dbf.delete(table, where)
    return True