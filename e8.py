import pandas as pd
data={"fruit":["apple","orange","banana","strawberry","kiwifruit"],
"year":[2001,2002,2001,2008,2006],
"time":[1,4,5,6,3]}
df=pd.DataFrame(data)
df["price"]=[150,120,100,300,150]
print(df)
