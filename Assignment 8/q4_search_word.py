# Q4: Search for a word in file and print line numbers
word = input("Enter word to search: ")
with open("notes.txt", "r") as f:
    for num, line in enumerate(f, 1):
        if word in line:
            print(f"Found at line {num}")