import numpy as np
a = np.random.randint(1,10,(2,3))
b = np.random.randint(1,10,(2,3))
print("Vertical Stack:\n", np.vstack((a,b)))
print("Horizontal Stack:\n", np.hstack((a,b)))
