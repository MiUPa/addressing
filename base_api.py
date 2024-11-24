import requests
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# BASE API OAuthエンドポイント
TOKEN_URL = "https://api.thebase.in/1/oauth/token"
# 注文情報のエンドポイント
ORDERS_URL = "https://api.thebase.in/1/orders"

# 環境変数からCLIENT_IDとCLIENT_SECRETを取得
BASE_CLIENT_ID = os.getenv("BASE_CLIENT_ID")
BASE_CLIENT_SECRET = os.getenv("BASE_CLIENT_SECRET")

# トークンを取得する関数


def get_access_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": BASE_CLIENT_ID,
        "client_secret": BASE_CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return access_token
    else:
        print(f"Failed to get access token: {response.status_code}")
        return None

# 注文情報を取得する関数


def get_order_info(order_id):
    access_token = get_access_token()
    if access_token is None:
        return None

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(f"{ORDERS_URL}/{order_id}", headers=headers)

    if response.status_code == 200:
        order = response.json()
        return order
    else:
        print(f"Failed to fetch order {order_id}: {response.status_code}")
        return None
