import json
from itertools import islice

import requests

COMPANY_NAME = "Tesla Inc"


def pcent_diff(yst: float, d_bf_yst: float) -> float:
    return float('{0:.2f}'.format(abs(((yst - d_bf_yst) / d_bf_yst) * 100)))


with open("day_36.json") as f:
    data = json.load(f)

response = requests.get(data["alphavantage"]["url"])
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

list_data = [[key, value["4. close"]] for (key, value) in islice(stock_data.items(), None, 2)]

diff = pcent_diff(float(list_data[0][1]), float(list_data[1][1]))

print(diff)

if diff > 0:
    url = data["newsapi"]["url"]
    parameters = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": data["newsapi"]["apiKey"]}

    res = requests.get(url, params=parameters)
    res_json = res.json()

    msg = [m["content"] for m in res_json["articles"][:3]]

    print(msg)
