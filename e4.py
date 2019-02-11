#P.233
import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
series=pd.Series(data,index=index)
conditions=[True,True,False,True,False]
print(series[conditions])
print()
print(series[series>=5][series<10])

items1=series.sort_index()
items2=series.sort_values()

print(items1)
print(items2)
