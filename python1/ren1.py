#6.1
vege ="potato"
n=[4,5,2,7,6]

print(len(vege))
print(len(n))
#print("\n")

alphabet=["a","b","c","d","e"]
alphabet.append("f") #append はリスト型の語尾につく加えることができるメソッド
print(alphabet)
print('sorted と sort の操作')
number=[1,3,2,5,7,9,4,6,10]
print(sorted(number))
print(number)
number.sort()
print(number)
print('大文字にして返すメソッドと数えたいオブジェクトの数を返すメソッド')
city="Tokyo"
print(city.upper())
print(city.count('o'))
print('format()メソッドの例')
fruit='banana'
color='yellow'
print('{}は{}です'.format(fruit,color))
