import numpy as  np
from scipy.sparse import csr_matrix
arr=np.array([[0,0,0],[0,1,0],[2,0,1]])
mat=csr_matrix(arr)
mat.eliminate_zeros()
mat2=csr_matrix(arr)
mat2.sum_duplicates()
print(mat2)
#print(mat)
print("Next")

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)