import numpy as np
p1 = np.array([2,3])
p2 = np.array([10,8])
dist = np.sqrt(((p2-p1)**2).sum())
print("Euclidean Distance:", dist)
