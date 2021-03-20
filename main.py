import json
from datetime import date, timedelta

import requests

COMPANY_NAME = "Tesla Inc"


def pcent_diff(num1: float, num2: float) -> float:
    return float('{0:.2f}'.format(abs((num1 - num2) / (num1 + num2) * 100)))


with open("day_36.json") as f:
    data = json.load(f)

response = requests.get(data["alphavantage"]["url"])
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

today = date.today()
y_day1 = str(today - timedelta(days=1))
y_day2 = str(today - timedelta(days=2))

n1 = float(stock_data[y_day1]["4. close"])
n2 = float(stock_data[y_day2]["4. close"])

diff = pcent_diff(n1, n2)

if diff > 0:
    print("Get News")

url = data["newsapi"]["url"]
parameters = {
    "q": COMPANY_NAME,
    "from": f"{y_day1}",
    "sortBy": "popularity",
    "apiKey": data["newsapi"]["apiKey"]}

res = requests.get(url, params=parameters)
res_json = res.json()

msg = [m["content"] for m in res_json["articles"][:3]]

print(msg)
