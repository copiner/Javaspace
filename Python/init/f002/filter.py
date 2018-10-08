
f = filter(None, [1,0,False,True])
print(f)
print(list(f))

def odd(x):
    return x%2
temp = range(10)
show = filter(odd, temp)
print(list(show))

print(list(filter(lambda x : x % 2, range(10))))


