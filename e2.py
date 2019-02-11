
import pandas as pd

index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
series=pd.Series(data,index=index)
print(series)
series=series.append(pd.Series({"pineapple":12}))
print()
print(series)
