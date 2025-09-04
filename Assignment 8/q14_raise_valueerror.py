# Q14: Raise ValueError if age < 18
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be 18 or above.")
else:
    print("You are eligible to vote.")