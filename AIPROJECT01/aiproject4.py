#import numpy as  np
#arr1=np.array([1,3,4,5,6,7,8])
#newarr=np.array_split(arr1,3)
#print(newarr)

import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
