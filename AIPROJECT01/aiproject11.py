import pandas as pd
import  matplotlib.pyplot as  plt
df=pd.read_csv('House_Price.csv')
#df.plot(kind='scatter',x='rainfall',y='age')
#plt.show()

# Scatter Plot() method
import pandas as pd

df = pd.read_csv('House_Price.csv')
#df['rainfall'].plot(kind = 'hist')
#plt.show()

df['teachers'].plot(kind='hist',color="red")
plt.show()