import pandas as pd
#read data from csv file
df = pd.read_csv('./pandas/bengaluru_house_prices.csv')
#print(df)

#print(df.info())
#print(df.describe())
#print(df.shape)

# df = df.head(100)
# print(df)

df = df.tail(50)
print(df)