
ll = ['Q', 4, 'U', 'E', 6, 'Y', 9.0]
ll.append("R")
print(ll)
ll.extend(["G","P"])
print(ll)

ll.insert(0, "A")
print(ll)

print(ll[3])

ll.remove("U")
print(ll)

del ll[5]
print(ll)

print(ll.pop())
print(ll)

xl = [1, 2, 3, 4, 5, 6, 7]
print(xl[1:3])
print(xl[:3])
print(xl)

al = xl[:]
print(al)
al = xl
xl.pop()
print(al)
xl.pop()
print(al)

list1 = [123, 456]
list2 = [234, 567]
print(list1<list2)
li = list1 + list2
print(li)

print(list1*3)

print(123 in list1)

print(dir(list))

