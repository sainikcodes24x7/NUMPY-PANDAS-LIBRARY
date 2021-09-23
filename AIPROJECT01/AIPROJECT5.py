import numpy as np
arr=np.array([[1,2],[2,3],[3,4],[4,5],[6,7],[4,8]])
newarr=np.array_split(arr,3)
print(newarr)

arr1=np.array([[1,2,5],[2,3,2],[3,4,9],[4,5,3],[6,8,7],[4,8,10]])
newarr = np.array_split(arr1, 3, axis = 1)

newarr2=np.hsplit(arr1,3)
print(newarr2)