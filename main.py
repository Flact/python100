import json
import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 36.778259
MY_LNG = -119.417931


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response.content)
    # print(type(response.content))

    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    # iss_position = (longitude, latitude)
    # print(iss_position)
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) & (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset | time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() & is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            with open('login.json') as f:
                data = json.load(f)
                email = data["gmail"]["email"]
                passwd = data["gmail"]["password"]
            conn.starttls()
            conn.login(user=email, password=passwd)
            conn.sendmail(from_addr=email, to_addrs=email,
                          msg="Subject:Look Up, 👆\n\nThe ISS is above you in the sky")
