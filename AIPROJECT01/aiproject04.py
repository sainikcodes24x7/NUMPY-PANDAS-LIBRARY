import numpy as  np
arr1=np.array([1,3,4])
arr2=np.array([4,5,6,])
arr31=np.array([1,3,4])
arr41=np.array([4,5,6])
arr=np.dstack((arr1,arr2,arr31,arr41))
print(arr)


print(np.concatenate((arr1,arr2)))

arr3=np.array([[1,23,4],[2,2,2]])
arr4=np.array([[4,5,6],[8,6,7]])
print(np.concatenate((arr3,arr4),axis=1))