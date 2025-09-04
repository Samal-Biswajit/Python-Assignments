# Q9: Same as Q5
nums = [10, 20, 30, 40, 50]
with open("numbers2.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")
with open("numbers2.txt", "r") as f:
    print([int(line.strip()) for line in f])