import sys
sys.path.append('./src/infra')

from pgsql_connection import PostgreSqlServerConnection


# Structural Patterns: Facade

def insert(table: str, data: dict, return_columns: list = None) -> list:
    """
    Insert data into a table
    Args:
        table(str): table name
        data(dict): data to be inserted
        return_columns(list): columns to be returned
    Returns:
        list: list of columns specified in return_columns
    """
    with PostgreSqlServerConnection() as conn:
        with conn.cursor() as cursor:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            if return_columns:
                sql += f' RETURNING {", ".join(return_columns)}'
            cursor.execute(sql, tuple(data.values()))
            fetch = []
            if return_columns:
                fetch = cursor.fetchone()
            conn.commit()
            return fetch

def update(table: str, data: dict, where: dict) -> bool:
    """
    Update data in a table
    Args:
        table(str): table name
        data(dict): data to be updated
        where(dict): where clause
    Returns:
        bool: True if data was updated, False otherwise
    """
    with PostgreSqlServerConnection() as conn:
        with conn.cursor() as cursor:
            columns = ', '.join([f'{column} = %s' for column in data.keys()])
            where_clause = ' AND '.join([f'{column} = %s' for column in where.keys()])
            sql = f'UPDATE {table} SET {columns} WHERE {where_clause}'
            cursor.execute(sql, tuple(data.values()) + tuple(where.values()))
            conn.commit()
            return True

def delete(table: str, where: dict) -> bool:
    """
    Delete data from a table
    Args:
        table(str): table name
        where(dict): where clause
    Returns:
        bool: True if data was deleted, False otherwise
    """
    with PostgreSqlServerConnection() as conn:
        with conn.cursor() as cursor:
            where_clause = ' AND '.join([f'{column} = %s' for column in where.keys()])
            sql = f'DELETE FROM {table} WHERE {where_clause}'
            cursor.execute(sql, tuple(where.values()))
            conn.commit()
            return True

def select(table: str, columns: list = None, where: dict = None, order_by: str = None, limit: int = None) -> list:
    """
    Select data from a table
    Args:
        table(str): table name
        columns(list): columns to be returned
        where(dict): where clause
        order_by(str): order by clause
        limit(int): limit clause
    Returns:
        list: list of tuples containing the data
    """
    with PostgreSqlServerConnection() as conn:
        with conn.cursor() as cursor:
            if columns:
                columns = ', '.join(columns)
            else:
                columns = '*'
            where_clause = ''
            if where:
                where_clause = ' AND '.join([f'{column} = %s' for column in where.keys()])
            order_by_clause = ''
            if order_by:
                order_by_clause = f'ORDER BY {order_by}'
            limit_clause = ''
            if limit:
                limit_clause = f'LIMIT {limit}'
            sql = f'SELECT {columns} FROM {table}'
            if where_clause:
                sql += f' WHERE {where_clause}'
            if order_by_clause:
                sql += f' {order_by_clause}'
            if limit_clause:
                sql += f' {limit_clause}'
            if where:
                cursor.execute(sql, tuple(where.values()))
            else:
                cursor.execute(sql)
            return cursor.fetchall()