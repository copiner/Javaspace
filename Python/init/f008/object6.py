class A:
    pass

class B(A):
    pass

class C():
    def __init__(self, x = 0):
        self.x = x

print(issubclass(B, A))

print(issubclass(B, B))

print(issubclass(B, object))

b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(isinstance(b, (A,B,C)))

c = C()
print(hasattr(c, 'x'))
#print(hasattr(c, x))# error

print(getattr(c, 'x'))
#print(getattr(c, 'y'))
print(getattr(c, 'y', 'no attribute y'))

setattr(c, 'y','Anna')

print(getattr(c, 'y', 'no attribute y'))

#delattr(c, 'y')

class D:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

d = D()
print(d.getSize())
print(d.x)
d.x = 18
print(d.x)
print(d.size)
print(d.getSize())

#del c.x
