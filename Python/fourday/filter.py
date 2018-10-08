
def is_odd(n):
    return n % 2 == 1
L=[1,2,3,4,5,6,7,8,9]
L=filter(is_odd, L)
print(list(L))

def not_empty(s):
    return s and s.strip()
L=['A','','B',None,'C',' ']
L = filter(not_empty,L)
print(list(L))

def level(s):
    return s == s[::-1]
l = filter(level, ['level','0909'])
print(list(l))

r = range(100, 1000)
ho = filter(level, map(str, r))
print(list(ho))
