
#lambda
f = lambda x: x*x
print(f)
print(f(5))

def build(x,y):
    return lambda: x*x + y*y
f = build(2,3)
print(f())
