#!/usr/bin/env python3

"""Flask app.

This program:

    - returns random health check information on http://localhost:80
    - returns historic health check information

Usage:

    Windows:

        python flaskapp.py
        (run from directory with flaskapp.py)

        python -m flaskapp
        (if directory with flaskapp.py is in sys.path)

    Unix:

        python3 flaskapp.py
        (run from directory with flaskapp.py)

        python3 -m flaskapp
        (if directory with flaskapp.py is in sys.path)

Package structure:

    flaskapp - package for Flask app:

        files
        folder for various project files

            sql.db
            sqlite3 database to hold health check information

        __init__.py
        package initialization file

        __main__.py
        allow program to be run by package name

        flask_sql.py
        SQL functionality (create table, store and retrieve data)

        main.py
        main program logic

    .gitattributes
    hold information about crlf options

    .gitignore
    ignore files for GIT

    flaskapp.py
    run program from command line

    README.md
    information about this program

    requirements.txt
    required python packages
"""

import random
from io import StringIO

from flask import Flask

from . import flask_sql


app = Flask(__name__)


@app.route('/')
def index():
    """Route for homepage. Return information about current health status.
    Store information in sqlite3 database.
    """

    message = "Health check done. Status: "
    if random.choice([True, False]):
        message += "OK"
    else:
        message += "ERROR"
    flask_sql.store_sql_data(message)
    return f"<h1>{message}</h1><a href='/history'>History of health checks</a>"


@app.route('/history')
def history():
    """Return information from sqlite3 database about previous health checks"""
    data_dict = flask_sql.retrieve_sql_data()
    if data_dict and data_dict is not None:
        string_obj = StringIO()
        string_obj.write("<h1>History of health checks</h1>"
                         "<table>"
                         "<tr><th>#</th><th>Date</th><th>Message</th></tr>")
        for data in data_dict:
            string_obj.write(f"<tr><td>{data}</td>"
                             f"<td>{data_dict[data][0]}</td>"
                             f"<td>{data_dict[data][1]}</td></tr>")
        string_obj.write("</table><br><a href='/'>Back</a>")
        return string_obj.getvalue()
    return "<h1>No health check information in the database</h1>"\
           "<a href='/'>Back</a>"
