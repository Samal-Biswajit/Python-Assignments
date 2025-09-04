# Q2: Read and print file content line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())