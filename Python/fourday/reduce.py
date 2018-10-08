
#reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

from functools import reduce
def add(x, y):
    return x + y

l=[1,3,5,7,9]

r= reduce(add, l)
print(r)

def fn(x, y):
    return x*10 + y

r=reduce(fn, l)
print(r)

dict = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9
        }
def chartoint(s):
    return dict[s]

r = reduce(fn, map(chartoint, '13579'))
print(r)

def atr2int(s):
    def fn(x,y):
        return x*10 + y
    def char2int(s):
        return dict[s]
    return reduce(fn, map(char2int, s))

def prod(L):
    def mul(x, y):
        return x*y
    return reduce(mul, L)
L=[1,2,3,4,5]
print(prod(L))

def normalize(name):
    name = name[0].upper()+name[1:].lower()
    return name
L1 = ['TIM', 'maNU','BobO']
L2 = list(map(normalize, L1))
print(L2)
