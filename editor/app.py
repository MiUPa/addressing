from flask import Flask, render_template
import os

# テンプレートとスタティックファイルのディレクトリを明示的に指定
template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, 
           template_folder=template_dir,
           static_folder=static_dir)

@app.route('/')
def index():
    # デバッグ情報を出力
    print("Current working directory:", os.getcwd())
    print("Template folder:", app.template_folder)
    print("Static folder:", app.static_folder)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)