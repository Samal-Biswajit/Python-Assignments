text = "Python is fun and Python is powerful"

# Convert to lowercase to count words case-insensitively
words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)