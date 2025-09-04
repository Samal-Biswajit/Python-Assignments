# Q13: Handle FileNotFoundError with finally
try:
    with open("random.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete")