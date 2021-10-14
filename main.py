#!/usr/bin/env python
import os

from flask import Flask

app = Flask(__name__)

if os.getenv("PORT") is None:
    port = 80
else:
    port = os.getenv("PORT")

# get name value from query string and cookie
@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World! From Raka"

if __name__ == "__main__":
    app.run(
            debug=True,
            host="0.0.0.0",
            port=port
            )
