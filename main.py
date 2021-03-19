import json

import requests

with open('weather_params.json') as f:
    parameters = json.load(f)

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()["hourly"]
conditions = [sub_data["weather"][0]["id"] for sub_data in data[:12] if sub_data["weather"][0]["id"] < 700]

print(len(conditions))
print(conditions)

