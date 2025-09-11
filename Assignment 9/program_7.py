import numpy as np
arr = np.arange(1,21)
div3 = arr[arr % 3 == 0]
print(div3)
