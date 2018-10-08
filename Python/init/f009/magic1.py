#__init__
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x + self.y)*2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(3, 4)
print(rect.getPeri())

print(rect.getArea())

#__new__
class CapStr(str): #inherit str
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

a = CapStr('Anna is a girl')
print(a)

#__del__
class C:
    def __init__(self):
        print('init')
    def __del__(self):
        print('del...')

a = C() #__init__
del a #__del__
