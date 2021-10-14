#!/usr/bin/env python
import os

from flask import Flask

app = Flask(__name__)

if os.getenv("PORT") is None:
    port = 5000
else:
    port = os.getenv("PORT")

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!"

#@app.route('/port')
#def port():
#    return "Hello World! " + port

if __name__ == "__main__":
    app.run(
            debug=True,
            host="0.0.0.0",
            port=port
            )
