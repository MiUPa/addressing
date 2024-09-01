import requests
from flask import Flask, request, redirect, render_template, session
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

client_id = os.environ.get("BASE_CLIENT_ID")
client_secret = os.environ.get("BASE_CLIENT_SECRET")
redirect_uri = os.environ.get("BASE_REDIRECT_URI")

app = Flask(__name__)

# セッションの設定
app.secret_key = os.environ.get("SECRET_KEY")


def get_authorization_url():
    """認可URLを生成する"""
    authorize_url = "https://api.thebase.in/1/oauth/authorize"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        # その他必要なパラメータ (e.g., scope)
    }
    return authorize_url + "?" + urllib.parse.urlencode(params)


def get_access_token(code):
    """アクセストークンを取得する"""
    token_url = "https://api.thebase.in/1/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.text}")


def get_orders(access_token, limit=10):
    """注文情報を取得する"""
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
    """トップページ"""
    authorize_url = get_authorization_url()
    return redirect(authorize_url)


@app.route('/callback')
def callback():
    """認可後のコールバック"""
    code = request.args.get('code')
    if code:
        try:
            access_token = get_access_token(code)
            session['access_token'] = access_token
            return redirect('/home')
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    else:
        return '認可コードが取得できませんでした'


@app.route('/home')
def home():
    """ホーム画面"""
    access_token = session.get('access_token')
    if access_token:
        try:
            orders = get_orders(access_token)
            return render_template('envelope_template.html', orders=orders)
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    else:
        return 'アクセストークンが見つかりません'


if __name__ == '__main__':
    app.run(debug=True)
