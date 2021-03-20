import json
from datetime import date

import requests


def pcent_diff(n1, n2):
    return float('{0:.2f}'.format(abs((n1 - n2) / (n1 + n2) * 100)))


with open("day_36.json") as f:
    data = json.load(f)

response = requests.get(data["alphavantage"]["url"])
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
# print(stock_data)
# print(response.json()["Time Series (Daily)"])

today = date.today()
yesterday = str(date(today.year, today.month, today.day - 1))
ereyesterday = str(date(today.year, today.month, today.day - 2))

# print(type(d))

x = pcent_diff(float(stock_data[yesterday]["4. close"]), float(stock_data[ereyesterday]["4. close"]))

print(type(x))
print(x)
