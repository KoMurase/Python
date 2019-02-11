#P.197
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print()
print("arr[0,2]=",arr[0,2])
#1行目以降と2列目までをとりだす
print(arr[1:,:2])
print()
#五行五列の行列から2行目以降と4列目までを取り出す
arr1=np.random.randint(0,11,(5,5))
print(arr1)
print()
print(arr1[2:,:4])
