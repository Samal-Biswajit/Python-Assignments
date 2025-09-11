import numpy as np
A = np.random.randint(1,10,(3,2))
B = np.random.randint(1,10,(2,4))
C = np.dot(A,B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Product:\n", C)
print("Shape of Result:", C.shape)
