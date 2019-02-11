import numpy as np
import pandas as pd
#from make_random_df import a1
#print("a1を使いまわしている？")
def make_random_df(index,columns,seed):
    np.random.seed(seed)
    df=pd.DataFrame()
    for column in columns:
        df[column]=np.random.choice(range(1,101),len(index))
        df.index=index
        return df

columns1=["apple","orange","banana"]
columns2=["orange","kiwifruit","banana"]
print("インデックスが1,2,3,4　カラムがcolumns1のDataFrameを作成する")
df_data1=make_random_df(range(1,5),columns1,0)
df_data2=make_random_df(np.arange(1,8,2),columns2,1)

df1=pd.concat([df_data1,df_data2],axis=0)
df2=pd.concat([df_data1,df_data2],axis=1)

print(df1)
print(df2)
