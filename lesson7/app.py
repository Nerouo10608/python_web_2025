<<<<<<< HEAD
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/knn")
def knn():
    return render_template("knn.html")
=======
from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/") # "/" 代表根目錄，即為首頁。
def index():
    return render_template("index.html")

@app.route("/decision_tree")
def decision_tree():
    tree_info = {
    "algorithm": "決策樹分類",
    "applications": ["垃圾郵件分類", "客戶流失預測", "疾病診斷"],
    "pros": ["容易理解", "不需要特徵縮放", "可視化清晰"]
}
    return render_template("decision_tree.html", tree_info = tree_info)
>>>>>>> bb1d9793f1518be19249ca92557bc5c2927f5b09

@app.route("/regression")
def regression():
    return render_template("regression.html")

<<<<<<< HEAD
@app.route("/test")
def test():
    return render_template("test.html")

def main():
    """啟動應用（教學用：啟用 debug 模式）"""
    # 在開發環境下使用 debug=True，部署時請關閉
    app.run(debug=True)
=======
@app.route("/knn")
def knn():
    return render_template("knn.html")

@app.route("/lesson6_1")
def lesson6_1():
    page_title = "我的首頁"
    users = [
        {"name": "小明", "is_vip": True},
        {"name": "小華", "is_vip": False},
        {"name": "小英", "is_vip": True}
    ]
    return  render_template("lesson6_1.html", title = page_title, user_list = users)

def main():
    """啟動應用(教學用：啟用 debug 模式)"""
    # 在開發環境下使用 debug = True，部屬時請關閉。
    app.run(debug = True)
>>>>>>> bb1d9793f1518be19249ca92557bc5c2927f5b09

if __name__ == "__main__":
    main()