from flask import Flask

HEALTH_STATUS = True

app = Flask(__name__)
app.debug = False


@app.route('/')
def index():
    message = "Health check done. Status: "
    if HEALTH_STATUS:
        return f"<h1>{message} OK</h1>"
    return f"<h1>{message} ERROR</h1>"
