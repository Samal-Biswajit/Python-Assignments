# Q15: Write user input to file, handle invalid file path
try:
    path = input("Enter file name to write: ")
    text = input("Enter text: ")
    with open(path, "w") as f:
        f.write(text)
    print("Data written successfully.")
except OSError:
    print("Error: Could not open/write file.")