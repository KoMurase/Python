#ソートと行列計算
#sort()は0を引数とすると列要素がソート,
#1を引数とすると行要素がソートされる
import numpy as np
arr=np.array([[8,4,2],[3,5,1]])

#argsort()メソッドを用いて出力してください
#argsort はsort後のインデックスを返すメソッド
print(arr.argsort())
print(np.sort(arr))
arr.sort(1)
print(arr)

#行列計算
#行列a,bの積はnp.dot(a,b),行列aのノルムはnp.lina.norm(a)
arr=np.arange(9).reshape(3,3)

print(np.dot(arr,arr))
vec=arr.reshape(9)
print(np.linalg.norm(vec))
