import sys

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "version": 1,
        "env": "staging",
        "python": sys.version.split()[0]
    })