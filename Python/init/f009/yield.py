def myGen():
    print('execuse')
    yield 1
    yield 2

#m = myGen()
#next(m)

#next(m)

for i in myGen():
    print(i)

def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a

for e in libs():
    if e > 100:
        break
    print(e, end = ' ')

a = [i for i in range(100) if not(i%2) and i%3]
print(a)

b= {i:i%2 == 0 for i in range(10)}

print(b)

c = {i for i in [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 3, 2, 1]}
print(c)

d = " i for i in 'Francis' "
print(d)

#generator
e = (i for i in range(10))
print(e)
print(next(e))
print(next(e))
print(next(e))

s1 = sum((i for i in range(100) if i % 2))
s2 = sum(i for i in range(100) if i % 2)
print(s1)
print(s2)

