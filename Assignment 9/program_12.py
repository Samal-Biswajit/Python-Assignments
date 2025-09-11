import numpy as np
coeff = np.array([[2,1],[1,-1]])
const = np.array([5,1])
sol = np.linalg.solve(coeff, const)
print("Solution:", sol)
