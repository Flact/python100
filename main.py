import requests

API_KEY = "cca441dbe68d12bf238a4e7c18e3ec22"
LAT = 36.778259
LON = -119.417931

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

print(response.json())
