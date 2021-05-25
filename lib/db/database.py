#!/bin/python3

import sqlite3
from sqlite3 import Error
DATABASE = "/home/vitualizz/Development/work/leedev/python_game_quiz/database.db"


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print("Connected to Sqlite: ", sqlite3.version)

    except Error as e:
        print("Error to connected to Sqlite: ", e)

    return conn


def get_conn():
    return create_connection(DATABASE)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)


def migrations(conn):
    sql_create_resultados_trivial_table = """
        CREATE TABLE IF NOT EXISTS resultados_trivial (
            id integer PRIMARY KEY,
            username text NOT NULL,
            score integer NOT NULL,
            finish_at text NOT NULL
        )
    """
    create_table(conn, sql_create_resultados_trivial_table)


def main():
    conn = get_conn()

    if conn is not None:
        migrations(conn)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
