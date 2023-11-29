import sqlite3

def connect_to_database(database_project):
    return sqlite3.connect(database_project)

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def fetch_data(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def close_connection(conn):
    conn.close()