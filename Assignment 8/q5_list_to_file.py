# Q5: Write list to file and read it back
nums = [10, 20, 30, 40, 50]
with open("numbers.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")
with open("numbers.txt", "r") as f:
    print([int(line.strip()) for line in f])