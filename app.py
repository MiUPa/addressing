from flask import Flask, jsonify
from base_api import get_order_info  # base_apiから関数をインポート

app = Flask(__name__)


@app.route('/address/<order_id>', methods=['GET'])
def get_order(order_id):
    order = get_order_info(order_id)  # base_apiの関数を使用
    if order:
        return jsonify(order)
    else:
        return "注文情報が見つかりませんでした", 404


@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
