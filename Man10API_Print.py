import requests

API_KEY = "b9ee475e-ae3c-433c-b391-11a6ae706e3d"
request_result = requests.get("https://api.man10.red/v1/mshop/shop/list",
                              headers={"Authorization": f"Bearer {API_KEY}"})

print("200が出れば成功|401が出れば失敗")
print(request_result)
