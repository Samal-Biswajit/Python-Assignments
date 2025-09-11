import numpy as np
arr = np.arange(1,37).reshape(6,6)
border = np.concatenate([arr[0,:], arr[-1,:], arr[1:-1,0], arr[1:-1,-1]])
arr[0,:] = arr[-1,:] = arr[:,0] = arr[:,-1] = 0
print("Border Elements:", border)
print("Modified Matrix:\n", arr)
