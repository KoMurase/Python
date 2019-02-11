import pandas as pd
data=[10,5,8,12,3]
index=["apple","orange","banana","strawberry","kiwifruit"]
series=pd.Series(data,index=index)
series_value=series.values
series_index=series.index

print(series_value)
print(series_index)
