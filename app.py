#!/usr/bin/env python
import os

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

# Debug related
@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/all', methods = ['POST']) 
def all():
    response_data = request.get_json()
    if response_data is None:
        return {}, 400
    food_list = response_data["foodList"]
    for a in food_list:
        print("food item " + str(a))

    # Creating mocked response
    mocked_response_json = json.load(open('mocked_response.json'))
    return jsonify(mocked_response_json), 200

if __name__ == "__main__":
    app.run(
            debug=True,
            host="0.0.0.0",
            port=port
            )
