from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # デバッグ情報を出力
    print("Current working directory:", os.getcwd())
    print("Template folder:", app.template_folder)
    print("Static folder:", app.static_folder)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)