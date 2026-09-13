import os
import sys
from flask import Flask, jsonify, render_template

app = Flask(__name__)

ENV = os.getenv("APP_ENV", "staging")
VERSION = "1.0.0"

@app.route("/")
def index():
    return render_template(
        "index.html",
        version=VERSION,
        env=ENV,
        python_version=sys.version.split()[0]
    )

@app.route("/api/info")
@app.route("/api")
def api_info():
    return jsonify({
        "version": VERSION,
        "env": ENV,
        "python": sys.version.split()[0],
        "status": "healthy"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)