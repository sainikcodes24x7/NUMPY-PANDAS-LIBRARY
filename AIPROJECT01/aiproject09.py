#PRINT FULL
import pandas as pd
df=pd.read_csv('House_Price.csv')
#print(df.to_string())

# To Show first and last five rows of Data file
import pandas as pd
df = pd.read_csv('House_Price.csv')
print(df)
print(df.head(10))
print(df.tail(2))