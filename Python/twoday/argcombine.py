# *args **kw  arguments keywords
def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ',c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ',c, 'd = ', d, 'kw = ', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b', x=100)
f2(1,2,d=99, ext=None)

args=(1,2,3,4,5)
keywords={'d':100, 'x':'timmy'}
f1(*args, **keywords)

arg=(1,2,3)
keyword={'d':100, 'x':'timmy'}
f2(*arg, **keyword)
