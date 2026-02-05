from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    welcome_text ="Joseph application"  # Simple computation
    return welcome_text


def multiply():
    a = 3
    b = 4
    return a * b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
