import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data1=[10,5,8,12,3]
data2=[30,25,12,10,8]
series1=pd.Series(data,index=index)
series2=pd.Series(data,index=index)
df=pd.DataFrame([series1,series2])
