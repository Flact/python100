import datetime as dt
import random
import smtplib

# to_add = "example@yahoo.com"
g_mail = "example@gmail.com"
g_pw = "example"

day_of_week = dt.datetime.now().weekday()
# print(day_of_week)

if day_of_week == 3:
    with open("quotes.txt", encoding="utf-8") as file:
        quote = file.readlines()
        # print(type(quote))  # <class 'list'>

    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(user=g_mail, password=g_pw)
        # It's needed to be encoded the msg, if not throw this(err):"UnicodeEncodeError"
        # to fix it use .encode("utf-8")
        conn.sendmail(from_addr=g_mail, to_addrs=g_mail,
                      msg=f"Subject:Monday Motivation\n\n{random.choice(quote)}".encode("utf-8"))
