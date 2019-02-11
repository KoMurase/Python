import numpy as np
arr1=np.array([1,2,3,4,5])
print("arr1"+str(arr1))

arr2=arr1
arr2[0]=100
#別の変数が元の変数にも影響されている
print("arr1"+str(arr1))
print("arr2"+str(arr2))
#ndarryをcopy()を使って別の変数に代入した場合の挙動を見に行きましょう
arr1=np.array([1,2,3,4,5])
print("arr1"+str(arr1))

arr2=arr1.copy()
arr2[0]=100

print("arr1"+str(arr1))
print("arr2"+str(arr2))
