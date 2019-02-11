#継承について
#class Medaka(Fish):
#class 新規クラス名（継承したいクラス名）:
class Fish:
    def __init__(self, name, build="ほね", eyelids=False):
        self.name = name
        self.build = build
        self.eyelids = eyelids

    def swim(self):
        print("こちらの魚は泳ぎます")

    def swim_back(self):
        print("こちらの魚は後ろ向きにも泳ぎます")

class Medaka(Fish):
    pass#passには親クラスをそのままという意味で

class Kingyo(Fish):
    def __init__(self, name, build="ほね", eyelids=False):
        self.name = '金魚ちゃん' + name + 'だよ'
        self.build = build + '　かな'
        self.eyelids = eyelids
n0=Fish("魚1(親クラス)")
print(n0.name)
print("骨格:",n0.build)
print("まぶた:",n0.eyelids)
n0.swim()
n0.swim_back()

n1=Fish("魚2(子クラス)")
print(n1.name)
print("骨格:",n1.build)
print("まぶた:",n1.eyelids)
n0.swim()
n0.swim_back()

n2=Kingyo("魚3(子クラス)")
print(n2.name)
print("骨格:",n2.build)
print("まぶた:",n2 j.eyelids)
n0.swim()
n0.swim_back()
