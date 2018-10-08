
d={'a':1, 'b':2, 'c':3}
for key in d:
    print(key)


for value in d.values():
    print(value)

for k, v in d.items():
    print(k +':'+ str(v))

for ch in 'ABCD':
    print(ch)

#judge type unable or able iterable
#bo = isinstance(123, Iterable)

#print(bo)

#enumerate
for i, value in enumerate(['A','B','C']):
    print(i,value)

for x, y in [(1,1),(2,4),(3,9)]:
    print(x,y)


