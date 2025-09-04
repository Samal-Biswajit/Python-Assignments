# Q8: Count number of words in a file
with open("notes.txt", "r") as f:
    text = f.read()
    print("Word count:", len(text.split()))