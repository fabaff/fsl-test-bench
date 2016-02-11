from flask import Flask
from flask import render_template

import time
#import pylinux.pylinux as pylinux

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!' + 'Time now ' + time.ctime()

@app.route("/uptime")
def uptime():
    return 'Test bench up for %s hours' % time.ctime() #str(pylinux.uptime())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
