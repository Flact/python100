import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.content)
# print(type(response.content))

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
