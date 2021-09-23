import  numpy as  np
arr=np.array([[1,4,2,7],[5,2,9,8]])
print(np.sort(arr,axis=1))

arr2=np.array([40,41,42,43])
x=np.array('True')

#import numpy as np
arr1=np.array([41,42,43,44])
x1=[True,False,True,False]
newarr=arr1[x1]
print(newarr)

arx=np.array([True,False,False,True])
print(np.sort(arx))

#Search from the Right Side
#import numpy as np
arr3 = np.array([6,8,7,9])
x2 = np.searchsorted(arr3, 7, side='right')
print(x2)