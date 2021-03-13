import random
import smtplib
from datetime import datetime as dt

import pandas as pd

g_mail = "example@gmail.com"
g_pw = "example"

today = [dt.now().month, dt.now().day]

data = pd.read_csv("birthdays.csv")
row = data[(data['month'] == today[0]) & (data['day'] == today[1])]  # Very Very important: if Selecting rows,
# based on multiple column conditions, wrap those condition with brackets

if not row.empty:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as f:
        msg = f.read().replace('[NAME]', row["name"].item())  # row["name"] returns a list that's why put .item()
        print(msg)
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=g_mail, password=g_pw)
            conn.sendmail(from_addr=g_mail, to_addrs=row["email"].item(),
                          msg=f"Subject:Happy Birthday\n\n{msg}")
