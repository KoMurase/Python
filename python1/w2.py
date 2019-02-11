#統計関数
import numpy as np

arr=np.arange(15).reshape(3,5)
print(arr)
print()

print("列ごとの平均を計算します")
print(arr.mean(axis=0))
print()

print("変数arrの行ごとの平均を計算をします")
print(arr.sum(axis=1))
print()

print("変数arrの最小値を出力します")
print(arr.min())
print()

print("変数arrのそれぞれの列の最大値のインデックス番号を出力します")
print(arr.argmax(axis=0))
