# Q3: Count words, characters, and lines in a file
with open("notes.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Lines:", text.count("\n") + 1)
    print("Words:", len(words))
    print("Characters:", len(text))