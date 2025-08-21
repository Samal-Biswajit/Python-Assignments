a = int(input("Enter Marks in 1st subject: "))
b = int(input("Enter Marks in 2nd subject: "))
c = int(input("Enter Marks in 3rd subject: "))
s = a+b+c
avg = s / 3
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)