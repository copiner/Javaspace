
print(type(123))
print(type(abs))

print(type('abc') == str)
print(type('abc') == type('123'))

import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)

print(isinstance('a', str))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3],(list, tuple)))
print(isinstance((1, 2, 3),(list, tuple)))

#print the all attributes and methods
#print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

class  MyDog(object):
    def __len__(self):
        return 10

dog = MyDog()
print(len(dog))

# getattr() setattr() hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
setattr(obj, 'y', 19)
y = getattr(obj, 'y')
z = getattr(obj, 'z', 404)
print(y)
print(z)
print(obj.y)

print(hasattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
