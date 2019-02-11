import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
series=pd.Series(data,index=index)
print(series)
series=series.drop("strawberry")
print(series)
