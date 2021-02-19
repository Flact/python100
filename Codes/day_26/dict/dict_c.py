# import random
#
# names = ["Aaaa", "Bbbb", "Cccccccc", "Ddddddd", "Eeeeeee", "Ffff"]
#
# student_scores = {student: random.randint(1, 100) for student in names}
#
# print(student_scores.items())
#
# passed_students = {student: mark for (student, mark) in student_scores.items() if mark > 50}
#
# print(passed_students)
# ********************************************************************
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {word: len(word) for word in sentence.split()}
#
# print(result)
# *****************************************************************

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

