import pandas as pd
import numpy as np
columns=["apple","orange","banana","strawberry","kiwifruit"]
df=pd.DataFrame()
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
df.index=range(1,11)
df=df.drop(np.arange(2,11,2))
#2から10までの数列を差が2になるように抜き出したもの
print(df)
df=df.drop("strawberry",axis=1)
print()
print(df)
