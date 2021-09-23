import  numpy as np
arr = np.array([1,3,4,4,5,4,4])
x = np.where(arr%2 == 0)
print(x)

arr1=np.array([2,3,4,6,5,7,8,9,])
y=np.searchsorted(arr1,5)
print(y)

arr2=np.array([[8,4,6,5,7,0],[1,5,3,4]])
x=np.sort(arr2)
print(x)

#import numpy as np
arr3 = np.array([6,7,8,9])
z = np.searchsorted(arr3, 7, side ='right')
print(z)

# using sort()
#import numpy as np
ar = np.array(['arkaprovo', 'sukanya', 'Shrijita'])
print(np.sort(ar))