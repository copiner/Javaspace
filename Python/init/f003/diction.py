

dicti = {}
x = dicti.fromkeys((1,2,3))
print(x)
y = dicti.fromkeys((1,2,3),'num')
print(y)
z = dicti.fromkeys((1,3),'yoyo')
print(z)

a = dicti.fromkeys(range(16),'hi')
print(a)

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

for item in a.items():
    print(item)

#print(a[12])

print(a.get(14,'no'))
print(a.get(16,'no'))

print(12 in a)
print(16 in a)

print(a)
a.clear()
print(a)

print(dicti)

b = {1:'one',2:'two',3:'three'}
e = b
c = b.copy()
print(id(e))
print(id(b))
print(id(c))

print(b.pop(2))
print(b.popitem())

b.setdefault(5, 'five')
print(b)

f = {1: 'calvin'}
b.update(f)
print(b)
