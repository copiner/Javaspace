
import functools
int2 = functools.partial(int, base=2)
v = int2('1000000')
print(v)

int2 = functools.partial(int, base=2)
print(int2('10010'))

#kw = { 'base':2 } int('10010', **kw)

max2 = functools.partial(max, 10)

print(max2(5,6,7))
#args = (10,5,6,7) max(*args)
