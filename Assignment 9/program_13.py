import numpy as np
arr = np.random.randint(1,101,20)
print("Original Array:", arr)
arr[arr > 50] = 50
arr[arr < 20] = 20
print("Modified Array:", arr)
