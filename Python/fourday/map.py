
def f(x):
    return x*x
l = [1,2,3,4,5,6,7,8,9]
r = map(f,l)
print(list(r))

s = map(str, l)
print(list(s))
