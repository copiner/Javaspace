#list
L=[x*x for x in range(10)]
print(L)
#generator
g=(x*x for x in range(10))
print(g)

for n in g:
    print(n)



ge=(x*x for x in range(10))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
