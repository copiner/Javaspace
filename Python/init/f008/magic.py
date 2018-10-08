#__init__(self)  constructor

class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print('kick %s...' % self.name)

a = Ball('H')
a.kick()

#name mangling
#private public
class Person:
    name = "Anna"
    __age = 18
    def getAge(self):
        return self.__age


p = Person()
print(p.name)
#print(p.age)
print(p.getAge())

