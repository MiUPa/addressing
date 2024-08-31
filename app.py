import requests
from flask import Flask, render_template
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()


app = Flask(__name__)


def get_authorization_url():
    """認可URLを生成する"""
    authorize_url = "https://api.thebase.in/1/oauth/authorize"
    params = {
        "response_type": "code",
        "client_id": os.environ.get("BASE_CLIENT_ID"),
        "redirect_uri": os.environ.get("BASE_REDIRECT_URI"),
        # その他必要なパラメータ
    }
    return authorize_url + "?" + urllib.parse.urlencode(params)


code = requests.args.get('code')


def get_access_token(code):
    token_url = "https://api.thebase.in/1/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": os.environ.get("BASE_CLIENT_ID"),
        "client_secret": os.environ.get("BASE_CLIENT_SECRET"),
        "redirect_uri": os.environ.get("BASE_REDIRECT_URI")
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=data, headers=headers)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        try:
            error_message = response.json()["error_description"]
        except json.JSONDecodeError:
            error_message = response.text
        print(f"Error: {error_message}")  # デバッグログ出力
        raise Exception(f"Failed to get access token: {error_message}")  # より具体的なエラーメッセージ


def get_orders(access_token, limit=10):
    orders_url = "https://api.thebase.in/1/orders"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"limit": limit}
    response = requests.get(orders_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["orders"]
    else:
        raise Exception("Failed to get orders")


@app.route('/')
def index():
    try:
        access_token = get_access_token()
        orders = get_orders(access_token)
        return render_template('envelope_template.html', orders=orders)
    except Exception as e:
        return str(e)  # 本番環境ではエラーの詳細を返さないようにする


if __name__ == '__main__':
    app.run(debug=True)
