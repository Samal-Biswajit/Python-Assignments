# Q7: Search for line numbers containing a word
word = input("Enter word to search: ")
with open("notes.txt", "r") as f:
    for num, line in enumerate(f, 1):
        if word in line:
            print("Word found in line", num)