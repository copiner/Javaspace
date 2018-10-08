class C:
    def __init__(self):
        self.x = "sth"

c = C()
print(c.x)
print(getattr(c, 'y', 'Anna'))

class A():
    def __init__(self, size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)

a = A()
a.x = 1
print(a.x)
print(a.size)
del a.x
print(a.size)


