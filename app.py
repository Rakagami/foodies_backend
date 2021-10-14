#!/usr/bin/env python
import os

from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/port')
def port():
    return "Hello World! " + str(port)

if __name__ == "__main__":
    app.run(
            debug=True,
            host="0.0.0.0",
            port=port
            )
