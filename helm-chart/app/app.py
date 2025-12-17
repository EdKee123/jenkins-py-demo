from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/add")
def add():
    try:
        a = float(request.args.get("a",""))
        b = float(request.args.get("b",""))
    except ValueError:
        return jsonify(error="invalid numbers"), 400
    return jsonify(result = a +b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)