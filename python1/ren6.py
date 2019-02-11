#ブルーインデックス参照
import numpy as np
arr1=np.arange(1,5)
print('arr1:',arr1)
arr2=np.array([2,4,6,7])
print(arr1[np.array([True,True,True,False])])
print(arr2[np.array([True,True,True,False])])

arr3=np.array([2,4,6,7])
print("arr3:",arr3)
print("arr3[arr%3==1]:",arr3[arr3%3==1])
