print("AI CODE IS WORKING...")
import numpy

print("Numpy version is...",numpy.__version__)

import matplotlib
print("Matplotlib version is...",matplotlib.__version__)

import pandas
print("pandas = ", pandas.__version__)
import sklearn
print("sklearn = ", sklearn.__version__)
import scipy
print("scipy = ", scipy.__version__)
#import seaborn
#print("seaborn = ", seaborn.__version__)

print("All AI Pluggins are installed and working successfully")

#Multiple plots
#Draw 2 plots

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

#plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()