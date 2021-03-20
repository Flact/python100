import requests
import json
from datetime import date

with open("day_37.json") as f:
    data = json.load(f)

graph_url = f"{data['endpoint']}/{data['user_params']['username']}/graphs"

pixel_url = f"{data['endpoint']}/{data['user_params']['username']}/graphs/{data['graph_config']['id']}"

today = date.today().strftime("%Y%m%d")

pixel_param = {
    "date": f"{today}",
    "quantity": "5.50"
}

# print(type(today))

res = requests.post(url=pixel_url, json=pixel_param, headers=data['headers'])
print(res.text)
