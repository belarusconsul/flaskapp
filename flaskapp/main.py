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

from flask import Flask, render_template

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
    return render_template("index.html", message=message)


@app.route('/history')
def history():
    """Return information from sqlite3 database about previous health checks"""
    data_dict = flask_sql.retrieve_sql_data()
    if data_dict and data_dict is not None:
        return render_template("history_success.html", data_dict=data_dict)
    return render_template("history_failure.html")
