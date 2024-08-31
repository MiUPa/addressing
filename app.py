import os
   from flask import Flask, render_template
   import requests

   app = Flask(__name__)

   def get_access_token():
       token_url = "https://api.thebase.in/1/oauth/token"
       data = {
           "grant_type": "client_credentials",
           "client_id": os.environ.get("BASE_CLIENT_ID"),
           "client_secret": os.environ.get("BASE_CLIENT_SECRET"),
           "redirect_uri": os.environ.get("BASE_REDIRECT_URI")
       }
       response = requests.post(token_url, data=data)
       if response.status_code == 200:
           return response.json()["access_token"]
       else:
           raise Exception("Failed to get access token")

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
           return str(e)

   if __name__ == '__main__':
       app.run(debug=True)