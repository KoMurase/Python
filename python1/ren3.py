import numpy as np
import time
from numpy.random import rand
#行列の大きさ
N=150
#行列の初期化します
matA=np.array(rand(N,N))
matB=np.array(rand(N,N))
matC=np.array([[0]*N for _ in range(N)])
#pythonのリスト使って計算する
#開始時間を取得します
start=time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
                matC[i][j]=matA[i][k]*matB[k][j]
print("Pythonの機能のみでの計算結果:%.2f"%float(time.time()-start))
#NumPyを使っての計算をします
#開始時間を取得します
start=time.time()
#NumPyを使って行列の掛け算を実行します
matC=np.dot(matA,matB)
#少数第二位の桁で打ち切っているのでNumPyは0.00[sec]と表示される
print("NumPyを使った場合の計算結果：%.2f"%float(time.time()-start))
