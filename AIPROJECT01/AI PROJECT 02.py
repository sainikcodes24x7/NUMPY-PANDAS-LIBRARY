import numpy as np
arr=np.array([1,2,3,4,6,5])
print(arr[1:5:2])
print(arr[-4:-1])
print(arr.dtype)

arr2=np.array(['Sainik','Reina','Razia'])
print(arr2)
print(arr2.dtype)


arr3= np.array([1,2,3,4], dtype ='i4')
print (arr3)
print ( arr3.dtype)

arr4=np.array([2,6,7,8,5,9],ndmin=3)
print(arr4)
print('Shape of array',arr4.shape)
