#p.241
import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data1=[10,5,8,12,3]
data2=[30,25,12,10,8]
data3=[30,12,10,8,25,3]
series1=pd.Series(data1,index=index)
series2=pd.Series(data2,index=index)

index.append("pineapple")
series3=pd.Series(data3,index=index)
df=pd.Series(data3,index=index)
df=pd.DataFrame([series1,series2])
df=df.append(series3,ignore_index=True)
print(df)
