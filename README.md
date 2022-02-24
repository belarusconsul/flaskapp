# Flask app


### Project for Python L2 Mentoring Program \#2


### Author: Nickolai Lychagin, Nickolai_Lychagin@epam.com
### Version 0.2, 24.02.2022

> This program:
>
> - returns random health check information on http://localhost:80
> - returns historic health check information
---
## USAGE

**Windows:**<br>
`python flaskapp.py` (run from directory with flaskapp.py) or<br>
`python -m flaskapp` (if directory with flaskapp.py is in sys.path)<br>
**Unix:**<br>
`python3 flaskapp.py`(run from directory with flaskapp.py) or<br>
`python3 -m flaskapp`(if directory with flaskapp.py is in sys.path)<br>

---
## FOLDER STRUCTURE

### flaskapp - package for Flask app:
#### files - folder for various project files
- sql.db - sqlite3 database to hold health check information
#### \_\_init\_\_.py - package initialization file
#### \_\_main\_\_.py - allow program to be run by package name
#### flask_sql.py - SQL functionality (create table, store and retrieve data)
#### main.py - main program logic

### .gitattributes - hold information about crlf options
### .gitignore - ignore files for GIT
### flaskapp.py - run program from command line
### README.md - information about this program
### requirements.txt - required python packages
