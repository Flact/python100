# import smtplib
#
# my_email_g = "sumududalamal6@gmail.com"
# my_email_y = "sumududalmal@yahoo.com"
#
# password_g = "xhBCB9*gi%CZ@*"
# password_y = "ircfhqvvplimttpy"  # Yahoo App password
#
# to_address_g = "sumududalamal6@gmail.com"
# to_address_y = "sumududalmal@yahoo.com"
#
# # Yahoo to Gmail
# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email_y, password=password_y)
#     connection.sendmail(from_addr=my_email_y,
#                         to_addrs=to_address_g,
#                         msg="Subject:Hello\n\nThis is the body of my email")
#
# # # Gmail to Yahoo
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email_g, password=password_g)
#     connection.sendmail(from_addr=my_email_g,
#                         to_addrs=to_address_y,
#                         msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

# for _ in range(100):
#     print(dt.datetime.now())
# Some Comment😁
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(type(now))  # <class 'datetime.datetime'>
# print(type(year))  # <class 'int'>
# print(type(month))  # <class 'int'>
# print(type(day_of_week))  # <class 'int'>
# print(year)
# print(month)
# print(day_of_week)  # Start with 0 (like index of array

# Create own datetime Object
# data_of_birth = dt.datetime(year=1996, month=2,
#                             day=29)  # If leave like this hour, sec, etc. set to default 0# ["1996-02-29 00:00:00"]
# print(data_of_birth)

# Or we can specify hour, sec, etc.
data_of_birth = dt.datetime(year=1996, month=2, day=29, hour=5)  # 1996-02-29 05:00:00
print(data_of_birth)
