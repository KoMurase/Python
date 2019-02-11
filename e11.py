import numpy as np
import pandas as pd

np.random.seed(0)
columns=["apple","orange","banana","strawberry","kiwifruit"]
df=pd.DataFrame()

for column in columns:
    df[column]=np.random.choice(range(1,11),10)
#range(開始後,終了後-1)です
df.index=range(1,11)
#loc[]を使ってdfの2行目から5行目までの4行と,"banan"、"kiwifruit"
#の2列を含むDataFrameをdfに代入してください
df=df.loc[[2,1,3,4,0],["banana","banana","banana","banana","banana"]]
print(df)
