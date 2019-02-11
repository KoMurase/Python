import pandas as pd
data0=["apple","orange","banana","strawberry","kiwifruit"]
data1=[10,5,8,12,3]
data2=[30,25,12,10,8]
series1=pd.Series(data1,index=data0)
series2=pd.Series(data2,index=data0)
df=pd.DataFrame([series1,series2])
df.index+=1
#本にはない方法
print(df)
