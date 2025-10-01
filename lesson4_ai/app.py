from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def index():
    return render_template("index.html", title="首頁")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

