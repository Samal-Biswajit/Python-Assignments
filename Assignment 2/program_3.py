a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
if (a>b) and (a>c):
    print("1st is largest")
elif (b>a) and (b>c):
    print("2nd is largest")
else:
    print("3rd is largest")