
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    marks = student_scores[key]
    if marks >= 91 and marks <= 100:
        student_grades[key] = "Outstanding"
    elif marks >= 81 and marks <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif marks >= 71 and marks <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)





