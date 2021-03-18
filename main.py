import json

import requests

with open('weather_params.json') as f:
    parameters = json.load(f)

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

print(response.json())
