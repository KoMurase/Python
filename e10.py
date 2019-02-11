import pandas as pd
data={"fruit":["apple","orange","banana","strawberry","kiwifruit"],
"yaer":[2001,2002,2001,2008,2006],
"time":[1,4,3,2,5]}
df=pd.DataFrame(data)
print(df)

#dfに対してdf.loc["インデックス","カラムのリスト"]と
#とすることで該当範囲のDataFrameを得ることができる
print("df.loc[インデックス,カラムのリスト]を使って抜き出したい箇所を表示します")
print(df.loc[[1,2],["time"]])
