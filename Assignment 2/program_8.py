a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
m = float(input("Enter m: "))
n = float(input("Enter n: "))
denominator = a * d - c * b
if denominator == 0:
    print("Error: Denominator is zero, no unique solution.")
else:
    x1 = (m * d - b * n) / denominator
    x2 = (n * a - m * c) / denominator
    print("x1 =", x1)
    print("x2 =", x2)