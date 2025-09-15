from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1 style="color:red">Hello! Flask!</h1>'

@app.route("/name")
def name():
    return '<h1>Hello! Route!</h1>'

if __name__ == "__main__":
    app.run(debug = True)