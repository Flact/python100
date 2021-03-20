import json
from datetime import date

import requests

with open("day_37.json") as f:
    data = json.load(f)

graph_url = f"{data['endpoint']}/{data['user_params']['username']}/graphs"

pixel_url = f"{graph_url}/{data['graph_config']['id']}"

today = date.today().strftime("%Y%m%d")

pixel_param = {
    "date": f"{today}",
    "quantity": "15.50"
}

update_pixel_param = {
    "quantity": "15.50"
}
pixel_update_url = f"{pixel_url}/20210319"

# res = requests.post(url=pixel_url, json=pixel_param, headers=data['headers'])
res = requests.put(url=pixel_update_url, json=update_pixel_param, headers=data['headers'])
print(res.text)
