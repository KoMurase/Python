import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
series=pd.Series(data,index=index)


data={"fruit":["apple","orange","banana","strawberry","kiwifruit"],
"year":[2001,2002,2001,2008,2006],"time":[1,4,5,6,3]}
df=pd.DataFrame(data)
print("Seriesデータ")
print(series)
print("\n")
print("DataFrameデータ")
print(df)
