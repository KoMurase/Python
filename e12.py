import pandas as pd
data={"frutis":["apple","orange","banana","strawberry","kiwifruit"],
"year":[2001,2003,2045,2012,2019],
"time":[1,2,3,4,5]}

df=pd.DataFrame(data)
print(df)
print("df.iloc['行番号','列番号'] とすることで指定したdataframeを取り出せる")
df=df.iloc[[1,3],[0,2]]
print(df)
