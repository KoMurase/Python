#sort P.253
import pandas as pd
data={"fruit":["apple","orange","banana","strawberry","kiwifruit"],
"time":[1,4,3,4,5],"year":[2001,2003,2004,2006,2001]}
df=pd.DataFrame(data)
print(df)
print()
df=df.sort_values(by="year",ascending=True)
print(df)
print()
df=df.sort_values(by=["time","year"],ascending=True)
print(df)
