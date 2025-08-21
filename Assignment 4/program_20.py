# Program 20
nums = [1, 7, 3, 6, 5, 6]
for i in range(len(nums)):
    if sum(nums[:i]) == sum(nums[i+1:]):
        print("Index:", i)
        break
else:
    print("No such index found")