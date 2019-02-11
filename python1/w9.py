import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
series=pd.Series(data,index=index)
items1=series[1:4]
items2=series[["apple","strawberry","banana"]]
print(items1)
print()
print(items2)
