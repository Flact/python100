


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total , n = 0 ,  0

for heght in student_heights:
    total += heght
    n += 1

avg = total / n
print(f"Average Height: {round(avg)}")

