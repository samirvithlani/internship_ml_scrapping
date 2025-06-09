#dataframe
import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(df)

#custom index
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['a','b','c'])
print(df)

#column index... task

data = {"Gujarat":[10,20,30,40],"Maharashtra":[50,60,70,80],"Rajasthan":[90,100,110,120]}
#df = pd.DataFrame(data)
df = pd.DataFrame(data, index=['a','b','c','d'])
#df = pd.DataFrame(data, index=[1,2,3,4]) dynami index
print(df)
