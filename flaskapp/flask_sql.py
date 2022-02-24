"""SQL functionality for flask app.

    Constants:

        SQLDB - Path to local file with SQL database (in 'files' folder).

    Functions:

        create_sql_table()
        Create SQL table to hold health check information.

        store_sql_data(message: str)
        Store health check information in SQL table.

        retrieve_sql_data() -> dict
        Retrieve information from SQL table to a dictionary.
"""

import os
import sqlite3

from datetime import datetime

SQLDB = os.path.join(os.path.dirname(__file__), "files", "sql.db")


def create_sql_table():
    """Create SQL table to hold health check information"""
    files_folder = os.path.dirname(SQLDB)
    if not os.path.exists(files_folder):
        os.mkdir(files_folder)
    conn = False
    try:
        conn = sqlite3.connect(SQLDB)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS healthcheck ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "date TEXT, "
                    "message TEXT);")
    except sqlite3.OperationalError as err:
        print(f"SQL table could not be created: {err}")
    finally:
        if conn:
            conn.close()


def store_sql_data(message):
    """Store health check information in SQL table.

    Parameters:
        message: str - Health check information.
    """

    conn = False
    try:
        conn = sqlite3.connect(SQLDB)
        cur = conn.cursor()
        cur.execute("INSERT INTO healthcheck(date, message) "
                    "VALUES(?, ?);",
                    (datetime.now(), message))
        conn.commit()
    except sqlite3.OperationalError as err:
        print(f"SQL table could not be updated: {err}")
    finally:
        if conn:
            conn.close()


def retrieve_sql_data():
    """Retrieve information from SQL table to a dictionary.

    Returns
        data_dict: dict - Dictionary of data from SQL table.
    """

    conn = False
    data_dict = {}
    try:
        conn = sqlite3.connect(SQLDB)
        cur = conn.cursor()
        cur.execute("SELECT date, message FROM healthcheck ORDER BY date DESC")
        row_num = 1
        for row in cur:
            data_dict[row_num] = [row[0][:-7], row[1][18:]]
            row_num += 1
        return data_dict
    except sqlite3.OperationalError as err:
        print(f"Information could not be retrieved from SQL table: {err}")
        return None
    finally:
        if conn:
            conn.close()
