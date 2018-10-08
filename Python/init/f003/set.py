#set
sett = {1, 2, 3, 4, 5}
print(type(sett))

se = {1,2,3,4,5,5,7}
print(se)

s = set([1,2,3,5,5,7])
print(s)

num = [1,2,3,3,2,6,5,8]
temp = []
for e in num:
    if e not in temp:
        temp.append(e)

print(temp)
number = list(set(num))
print(number)

s.add(9)
print(s)
s.remove(5)
print(s)

fro = frozenset([1,2,3,4,5])
print(fro)
