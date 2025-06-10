import pandas as pd
df =pd.read_csv("./pandas/Movieratingdata1.csv")
pd.set_option("display.max_column",None)
df.replace(to_replace="not available",value=None,inplace=True)
df.replace(to_replace=["not available","not mension"],value=None,inplace=True)
#print(df.info())
#df.replace([1,2,3,4,5,6,7,8,9],[1,1,1,1,1,1,1,1,1],inplace=True)
#null
#df = df.isnull()
#print(df.isnull().sum())
#df = df.dropna()
#df = df.dropna(axis=0)
#df = df.dropna(axis=1)
#df = df.dropna(how="any")
#df = df.dropna(subset=["RATING","PRODUCTION_YEAR"])


#df = df.fillna(7)
df = df.fillna({"MOVIE_TITLE":"Unknown","RATING":0})

print(df)