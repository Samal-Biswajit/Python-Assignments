# Q11: Handle ValueError and ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input! Enter numbers only.")
except ZeroDivisionError:
    print("Denominator cannot be zero!")