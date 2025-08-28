# Program to store and display book details

# Store book details in a dictionary
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 299.99
}

# Iterate through the dictionary and print each key and value
for key, value in book.items():
    print(f"{key}: {value}")