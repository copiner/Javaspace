#类定义、类对象C、实例对象a b c
class C:
    count = 0

a = C()
b = C()
c = C()
print(a.count)
print(b.count)
print(c.count)

print(C.count)

c.count += 10
print(a.count)
print(b.count)
print(c.count)


print(C.count)

C.count +=100

print(a.count)
print(b.count)
print(c.count)


print(C.count)


