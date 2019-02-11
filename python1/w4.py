#添削問題P.212
####問題####
#各要素が0~30の整列の行列(5X3)を変数arrに代入してください
#変数arrを転置してください
#変数arrの2,3,4列のみの行列を変数arr1に代入してください
#変数arr1を行でソートしてください
#各列の平均を出力してください

import numpy as np
from numpy.random import randint

arr=randint(0,31,(5,3))
print(arr)
print()
print(arr.T)
print()
arr=arr.T[:,1:4]
print(arr)
print()
arr1=arr.T[:,1:4]
arr1.sort(1)
print(arr1)
print()
print(arr1.mean(axis=0))
