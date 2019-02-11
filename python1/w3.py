#ブロードキャストP.210
import numpy as np
print("0~15の整数値を持つ3X5のndarry配列Xを生成します")

x=np.arange(15).reshape(3,5)
print(x)
print()

print("o~4の整数値をもつ1X5のndarry配列yを生成します")
y=np.array([np.arange(5)])
print(y)
print()

z=x-y
print(z)
