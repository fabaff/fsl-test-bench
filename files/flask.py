"""Simple Flask application."""
import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Default route for the server."""
    return f"Hello World! Time: {time.ctime()}"


@app.route("/uptime")
def uptime():
    """Route for the server's uptime."""
    return f"Test bench up for {time.ctime()} hours"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
