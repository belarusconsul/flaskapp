#!/usr/bin/env python3

from flaskapp.main import app

if __name__ == "__main__":
    app.run(host="localhost", port=80)
