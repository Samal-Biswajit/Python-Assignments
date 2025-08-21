# Program 12
lst = [10, 50, 20, 80, 30]
unique = list(set(lst))
unique.sort()
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Not enough unique elements")