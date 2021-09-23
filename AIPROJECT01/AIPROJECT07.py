import pandas as pd
mydataset={
    'cars':["BMW","ALTO","MERCEDES"],
    'pass':[3,4,5]
}
myvar=pd.DataFrame(mydataset);
print(myvar)

a=[1,3,5]
myvar2=pd.Series(a)
print(myvar2)

a=[1,3,5]
myvar2=pd.Series(a,index=["a","b","c"])
print(myvar2)

print(pd.__version__)

# Create a simple Pandas Series from a Dictionary
import pandas as pd
calories = {"day1":420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Create a simple Pandas Series from a Dictionary
import pandas as pd
calories = {"day1":420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


subscribers={"Day1":500,"Day2":750,"Day3":920}
myvar=pd.Series(subscribers,index=["Day1","Day2","Day3"])
print(myvar)