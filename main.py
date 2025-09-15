#todo:請建立一個Flask應用程式，並在根路由('/')上設置一個視圖函數，該函數返回"Hello, World!"字串作為響應。
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"
if __name__ == '__main__':
    app.run(debug=True)