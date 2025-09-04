# Q12: Square of number with try-except-else
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("Square:", n*n)