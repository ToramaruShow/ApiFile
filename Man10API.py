# import json
# import requests
# from flask import Flask, render_template
#
# # API_KEYs = "b9ee475e-ae3c-433c-b391-11a6ae706e3d"
# # request_result = requests.get("https://api.man10.red/v1/mshop/shop/list",
# #                               headers={"Authorization": f"Bearer {API_KEYs}"})
# # data = request_result.json()
# #
# # for shop_data in data["data"]:  # 1店舗(?)ずつデータを入れていく
# #     print(data)
# #     print(shop_data["name"], shop_data["money"])
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return render_template('ShopList.html')
#
#
# @app.route("/ShopList.html", methods=["POST"])
# def result():
#     API_KEY = "b9ee475e-ae3c-433c-b391-11a6ae706e3d"
#     print(API_KEY)
#     request_result = requests.get("https://api.man10.red/v1/mshop/shop/list",
#                                   headers={"Authorization": f"Bearer {API_KEY}"})
#     data = request_result.json()
#     json_data = json.dumps(data)
#     Count = int(0)
#     name = []
#     print(data)
#     for shop_data in data["data"]:  # 1店舗(?)ずつデータを表示
#         print(shop_data["name"], shop_data["money"])
#         name.insert(Count, shop_data["name"])
#         Count += 1
#     return render_template('/ShopList.html', JSONDATA=request_result.json(), COUNTER=Count, NAME=data)
#
#
# app.run(host="0.0.0.0", port=5000, debug=True)

# API_KEY = "b9ee475e-ae3c-433c-b391-11a6ae706e3d"

from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    API_KEY = str(request.form['API'])
    if API_KEY is None or API_KEY != "":
        response = requests.get("https://api.man10.red/v1/mshop/shop/list",
                                headers={"Authorization": f"Bearer {API_KEY}"})
        if response.status_code == 200:
            data = response.json()
            print(data)
            return render_template('APIKey.html', data=data)
        else:
            return 'Error: APIキーが間違っています！'
    else:
        return render_template('APIKey.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
