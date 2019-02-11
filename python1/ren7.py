#P.194
import numpy as np
#変数arrに2次元配列を代入してください
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
#変数arrの行列の各次元ごとの要素数を出力してください
print(arr.shape)
#変数arrを4行2に変換してください
print(arr.reshape(4,2))
#数学の転置行列だと思えばよい

arr1=np.random.randint(0,11,(5,5))
print("arr1:\n",arr1)
print("arr1[1]=",arr1[1])
print("arr1[1,1:]",arr1[1,1:])
