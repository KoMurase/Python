#p.198 axisについて
#axis:軸.地軸.中心線
import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

arr1=np.array([[1,2,3],[4,5,12],[15,20,22]])

print(arr1.sum(axis=1))
