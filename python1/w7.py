import pandas as pd
index=["apple","orange","banana","strawberry","kiwifruit"]
data=[10,5,8,12,3]
#indexとdataを含むSeriesを作成し,Seriesに代入してください
Series=pd.Series(data,index=index)
print(Series)
