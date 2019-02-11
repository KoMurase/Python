#214 総合添削問題
import numpy as np
np.random.seed(0)#乱数の初期化,seedは乱数を固定する
#縦の長さ、横の大きさを渡されたときに乱数で指定の大きさの画像を生成する関数です
def make_image(m,n):

    image=np.random.randint(0,6,(n,m))

    return image

#渡された行列の一部を変更する関数です
def change_little(matrix):
    #与えられた行列の形を取得し、shapeに代入してください
    shape=matrix.shape
    #行列の各成分について、変更するかしないかを
    #ランダムに決めた上で変更する場合は0~5のいずれかの整数に
    #ランダムに入れ替えてください
    for i in range(shape[0]):
        for j in range(shape[1]):
            if np.random.randint(0,2)==1:
                matrix[i][j]=np.random.randint(0,6,1)
    return matrix

#ランダムに画像を作成します
image1=make_image(3,3)
print(image1)
print()

#ランダムに変更を適用します
image2=change_little(np.copy(image1))
print(image2)
print()

image3=image1-image2
print(image3)
print()
image3=np.abs(image3)
print(image3)
