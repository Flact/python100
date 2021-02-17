with open("file1.txt", "r") as f1:
    nu1 = f1.readlines()

with open("file2.txt", "r") as f2:
    nu2 = f2.readlines()

result = [int(n) for n in nu1 if n in nu2]
print(result)
