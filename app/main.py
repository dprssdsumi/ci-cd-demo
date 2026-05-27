from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CI/CD Demo API", "status": "running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return jsonify({"result": a - b})

@app.route("/reverse/<string:text>")
def reverse(text):
    return jsonify({"result": text[::-1]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
