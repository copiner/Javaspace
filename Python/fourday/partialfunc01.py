
v = int('12345', base = 8)
print(v)

v = int('12345', base = 16)
print(v)

v = int('12345')
print(v)

def int2(x, base=2):
    return int(x, base)
v = int2('1000000')
print(v)

