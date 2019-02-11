#p.260 まとめ
import pandas as pd
import numpy as np

index=["growth","mission","ishikawa","pro"]
data=[50,7,26,1]
series=pd.Series(data,index=index)
print(series)
print()

aidemy=series.sort_index()
print(aidemy)
print()
aidemy1=pd.Series([30],["tutor"])
aidemy2=series.append(aidemy1)#append追加する
print(aidemy1)
print()
print(aidemy2)
print()
df=pd.DataFrame()
for index in index:
    df[index]=np.random.choice(range(1,11),10)
    #range(開始行数,終了行数-1)です
df.index=range(1,11)
aidemy3=df.loc[range(2,6),["ishikawa"]]
print(df)
print()
print(aidemy3)
