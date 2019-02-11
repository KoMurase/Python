#P.249
import numpy as np
import pandas as pd
np.random.seed(0)
columns=["apple","orange","banan","strawberry","kiwifruit"]

#DataFrameを生成し、列を追加する
df=pd.DataFrame()
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
df.index=range(1,11)

df=df.iloc[[1,2,3,4],[2,4]]

print(df)
