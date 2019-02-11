#path='test.txt'

#with open(path) as f:
#    s=f.read()
#    print(type(s))
#    print(s)

path_w='data.text'
s=input('何か書いて')
with open(path_w,mode='w') as f:
    f.write(s)

with open(path_w) as f:
    print(f.read())
