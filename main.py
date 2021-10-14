import os

from flask import Flask

app = Flask(__name__)

# get name value from query string and cookie
@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World! From Raka"

if __name__ == "__main__":
    app.run(
            debug=True,
            host="0.0.0.0",
            port=5000
            )
