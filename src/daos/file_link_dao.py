from database_facade import *
import sys
sys.path.append('./src')
sys.path.append('./src/models')

from file_link import FileLink
from helper import valida_autenticacao

@valida_autenticacao
def create_file_link(file_link: FileLink, *args, **kargs) -> FileLink:
    """
    Creates a new file_link in the database.
    Args:
        file_link: FileLink object to be created.
    """
    data = {
        'file_name': file_link.name,
        'user_id': file_link.user_id
    }
    id = insert('file', data, return_columns=('file_id',))[0]
    file_link._id = id
    return file_link

@valida_autenticacao
def get_file_links_by_user_id(user_id: int, *args, **kargs) -> list:
    """
    Gets file_links from the database by their user id.
    Args:
        user_id: User id.
    Returns:
        List of FileLink objects.
    """
    table = 'file'
    columns = ('file_name', 'user_id', 'file_id')
    where = {'user_id': user_id}
    fetch = select(table, columns, where)
    return [FileLink(*f) for f in fetch] if fetch else None

@valida_autenticacao
def update_file_link(file_link: FileLink, *args, **kargs) -> bool:
    """
    Updates a file_link in the database.
    Args:
        file_link: FileLink object to be updated.
    Returns:
        Boolean indicating if the file_link was updated.
    """
    data = {
        'file_name': file_link.name,
        'user_id': file_link.user_id
    }
    where = {'file_id': file_link._id}
    return update('file', data, where)

@valida_autenticacao
def delete_file_link(file_id: int, *args, **kargs) -> bool:
    """
    Deletes a file_link in the database.
    Args:
        id: FileLink id.
    Returns:
        Boolean indicating if the file_link was deleted.
    """
    where = {'file_id': file_id}
    return delete('file', where)