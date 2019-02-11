import numpy as np
import pandas as pd
np.random.seed(0)
columns=["apple","orange","banana","strawberry","kiwifruit"]
df=pd.DataFrame()
for column in columns:
    df[column]=np.random.choice(range(1,11),10)
df.index=range(1,11)
df=df.sort_values(by=["apple","orange","banana","strawberry","kiwifruit"],ascending=True)
print(df)
