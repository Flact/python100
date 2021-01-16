# with open("weather_data.csv") as data_set:
#     data = data_set.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_set:
#     data = csv.reader(data_set)
#     temperature = []
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

df = pandas.read_csv("weather_data.csv")
# print(type(df))
# print(type(df["temp"]))

# data_dict = df.to_dict()
# print(data_dict)

temp_list = df["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

avg_temp = df["temp"].mean()
# print(avg_temp)

max_temp = df["temp"].max()
# print(max_temp)

# print(df["condition"])  # this
# print(df.condition)  # or this

# print(df[df.day == "Monday"])  # print selected row

# print(df[df.temp == df.temp.max()])

# temp = df.temp[df.day == "Monday"]
# temp_to_F = temp * 9 / 5 + 32
# print(temp_to_F)

data_dict = {
    'animals': ['falcon', 'dog', 'spider', 'fish'],
    "num_legs": [2, 4, 8, 0],
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new-data.csv")
