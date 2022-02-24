#!/usr/bin/env python3
import os.path

from flaskapp.flask_sql import SQLDB, create_sql_table
from flaskapp.main import app


if __name__ == "__main__":
    if not os.path.exists(SQLDB):
        create_sql_table()
    app.run(host="localhost", port=80)
