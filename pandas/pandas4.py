import pandas as pd
df = pd.read_csv("./pandas/bengaluru_house_prices.csv")
#print(df)
#print(df.loc[[0]])
#print(df.loc[[0,1,2]])
#print(df.loc[10,"availability"])
#print(df.loc[1:10,"availability"])

#print(df.iloc[8:15])
print(df)
pd.set_option("display.max_rows",None)
pd.set_option("display.max_column",None)
print(df)
