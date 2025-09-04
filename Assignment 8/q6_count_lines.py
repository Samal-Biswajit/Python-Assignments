# Q6: Count number of lines in a file
with open("notes.txt", "r") as f:
    print("Total lines:", sum(1 for _ in f))