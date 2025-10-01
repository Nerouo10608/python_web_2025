from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/") # "/" 代表根目錄，即為首頁。
def hello_world():
    return render_template("index.html")

def main():
    """啟動應用(教學用：啟用 debug 模式)"""
    # 在開發環境下使用 debug = True，部屬時請關閉。
    app.run(debug = True)

if __name__ == "__main__":
    main()