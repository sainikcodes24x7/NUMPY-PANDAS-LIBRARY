# Create a Dataframe
import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]

}
df=pd.DataFrame(data)
print(df)
print(df.loc[[0,1]])
df=pd.DataFrame(data,index=["DAY1","DAY2","DAY3"])
print(df)
print(df.loc["DAY1"])