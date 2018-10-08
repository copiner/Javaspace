
#abs
x=abs(-10)
f = abs
v = f(-10)
print(x, v)

def add(x, y, f):
    return f(x) + f(y)

v = add(-5, 6, abs)
print(v)
