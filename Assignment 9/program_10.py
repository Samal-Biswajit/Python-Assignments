import numpy as np
mat = np.random.rand(4,4)
mean_cols = mat.mean(axis=0)
res = mat - mean_cols
print("Original Matrix:\n", mat)
print("After Subtracting Column Means:\n", res)
