from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!! - Yuhooo Your Flask App is running "


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
