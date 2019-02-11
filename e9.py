import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data1=[10,5,8,12,3]
data2=[30,25,12,10,8]
series1=pd.Series(data1,index=index)
series2=pd.Series(data2,index=index)

new_column=pd.Series([15,7],index=[0,1])
df=pd.DataFrame([series1,series2])

df["mango"]=new_column

print(df)
