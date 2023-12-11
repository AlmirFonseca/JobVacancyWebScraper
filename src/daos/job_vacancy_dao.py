from database_facade import *
import sys
sys.path.append('./src')
sys.path.append('./src/models')

from job_vacancy import JobVacancy
from helper import valida_autenticacao

@valida_autenticacao
def create_job_vacancy(job_vacancy: JobVacancy, *args, **kargs) -> JobVacancy:
    """
    Creates a new job_vacancy in the database.
    Args:
        job_vacancy: JobVacancy object to be created.
    """
    data = {
        'job_name': job_vacancy.name,
        'job_email': job_vacancy.email,
        'job_link': job_vacancy.link,
    }
    id = insert('job_vacancy', data, return_columns=('job_id',))[0]
    job_vacancy._id = id
    return job_vacancy

@valida_autenticacao
def get_job_vacancies(*args, **kargs):
    """
    Gets job_vacancies from the database.
    Returns:
        List of JobVacancy objects.
    """
    table = 'job_vacancy'
    columns = ('job_name', 'job_email', 'job_link', 'job_id')
    fetch = select(table, columns)
    return [JobVacancy(*f) for f in fetch] if fetch else None

@valida_autenticacao
def get_job_vacancy(id: int, *args, **kargs) -> JobVacancy:
    """
    Gets a job_vacancy from the database.
    Args:
        id: job_vacancy id.
    Returns:
        JobVacancy object.
    """
    table = 'job_vacancy'
    columns = ('job_name', 'job_email', 'job_link', 'job_id')
    where = {'job_id': id}
    fetch = select(table, columns, where)
    return JobVacancy(*fetch[0]) if fetch else None