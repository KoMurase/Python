#p.250 and p.251
import pandas as pd
import numpy as np
data={"fruit":["apple","orange","banana","strawberry","kiwifruit"],
"year":[2019,2020,2021,2022,2045],
"time":[1,4,5,6,3]}

df=pd.DataFrame(data)
df_1=df.drop(range(0,2))
df_2=df.drop("year",axis=1)
print(df_1)
print()
print(df_2)
