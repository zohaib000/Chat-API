from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    return jsonify({"response": "Output data will behere"})


if __name__ == "__main__":
    app.run(debug=True)
