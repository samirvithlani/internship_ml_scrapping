import pandas as pd
#pandas series
a = pd.Series([40,45,60,70,"8",90.1,123])
#print(a)

#index
a = pd.Series([40,45,60,70,"8",90.1,123], index=['a','b','c','d','e','f','g'])
#print(a)

#element access
#print(a['g'])

#dictionary to series
data = {"Gujarat": 60, "Maharashtra": 70, "Rajasthan": 80}
a = pd.Series(data)
#print(a)

#series slicing
print(a[1:3])  # Slicing from index 1 to 2 (exclusive of 3)


#mathematical operations

x1 = pd.Series([1, 2, 3, 4])
x2 = pd.Series([10, 20, 30, 40])

add = x1 + x2 # Addition
print("Addition:\n", add)