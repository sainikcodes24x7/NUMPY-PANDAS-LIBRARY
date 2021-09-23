from scipy import constants
print(constants.pi)

# Constants are helpful in scientific Data interpretation
from scipy import constants
print(dir(constants))

from scipy import constants
print(constants.atmosphere)

# Sparse Data
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))
arr2=csr_matrix(arr).data
print(arr2)


arx=np.array([[1,0,0],[6,0,3],[0,0,0],[1,0,1]])
print(csr_matrix(arx).count_nonzero())