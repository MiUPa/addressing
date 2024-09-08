import os
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# BASE APIの設定
BASE_API_KEY = os.getenv('BASE_API_KEY')
BASE_URL = 'https://api.thebase.in/1/orders'


def get_orders():
    headers = {
        'Authorization': f'Bearer {BASE_API_KEY}'
    }
    print(f"API Key: {BASE_API_KEY}")
    response = requests.get(BASE_URL, headers=headers)
    print(response.json())  # データをターミナルに出力して確認
    return response.json()


@app.route('/orders')
def orders():
    orders_data = get_orders()
    return jsonify(orders_data)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
