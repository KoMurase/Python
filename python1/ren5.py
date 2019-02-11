import numpy as np
#Pythonのリストでスライスを用いた場合の挙動を確認しよう
#arange()は等差数列を生成するメソッド
arr_List=[x for x in range(10)]
print('リスト型のデータです')
print('arr_List:',arr_List)

print()
arr_List_copy=arr_List[:]
arr_List_copy[0]=100

print("リストのスライスではコピーが作られるので,arr_Listにはarr_List_copyの変更が反映されない")
print("arr_List:",arr_List)
print()

#Numpyのndarrayでスライスを用いた場合での挙動を確認する
arr_NumPy=np.arange(10)
print("Numpyのndarryデータです")
print("arr_Numpy:",arr_NumPy)
print()

arr_NumPy_view=arr_NumPy[:]
arr_NumPy_view[0]=100

print("NumPyのスライスではview(データが格納されている場所の情報)が代入されるので、arr_NumPy_viewの変更がarr_NumPyに反映される")
print("arr_NumPy:",arr_NumPy)
print()

#Numpyのndarryでcopy()を用いた場合での挙動を見ていきましょう
arr_NumPy=np.arange(10)
print("NumPyのndarryでcopy()を用いた場合での挙動です")
print("arr_NumPy:",arr_NumPy)
print()
arr_NumPy_copy=arr_NumPy[:].copy()
arr_NumPy_copy[0]=100

print("copy()を用いた場合は、コピーが生成されるのでarr_NumPy_copyはarr_NumPyに影響を与えない")
print("arr_NumPy:",arr_NumPy)
print("arr_NumPy_copy:",arr_NumPy_copy)
