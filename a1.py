#P.262~dataframeの連結
import pandas as pd
import numpy as np

#指定のインデックスとカラムをもつDataFrameを
#乱数によって作成する関数
def make_random_df(index,columns,seed):
    np.random.seed(seed)   #seedとすることでランダムな数を生成し固定する
    df=pd.DataFrame()
    for column in columns:
        df[column]=np.random.choice(range(1,100),len(index))
    df.index=index
    return df
#インデックス、カラムが一致しているDataFrameを作成します
columns=["apple","orange","banana"]
df_data1=make_random_df(range(1,5),columns,0)
df_data2=make_random_df(range(1,5),columns,1)
print(df_data1)
print()
print(df_data2)
print("縦方向に連結します")
df_data3=pd.concat([df_data1,df_data2],axis=0)
print(df_data3)
print("横方向に連結します")
df_data4=pd.concat([df_data1,df_data2],axis=1)
print(df_data4)
