import pandas as pd

df1 = pd.DataFrame({'a':[1,2,3,3], 'b':[4,5,6,6]})
df2 = pd.DataFrame({'a':[2,2,3], 'b':[4,5,6]})

print(df1)
print(df2)

print(df1.merge(df2, how='outer',indicator=True))
print(df1.merge(df2,on='a', how='outer',indicator=True))