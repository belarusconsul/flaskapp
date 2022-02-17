#!/usr/bin/env python3

"""Flask app.

This program:

    - returns "Health check done. Status: OK" on http://localhost:80

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

        __init__.py
        package initialization file

        __main__.py
        allow program to be run by package name

        main.py
        main program logic

    .gitignore
    ignore files for GIT

    flaskapp.py
    run program from command line

    README.md
    information about this program

    requirements.txt
    required python packages
"""

from flask import Flask

HEALTH_STATUS = True

app = Flask(__name__)
app.debug = False


@app.route('/')
def index():
    """Route for homepage. Return information about health status"""
    message = "Health check done. Status: "
    if HEALTH_STATUS:
        return f"<h1>{message} OK</h1>"
    return f"<h1>{message} ERROR</h1>"
