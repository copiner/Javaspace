
#__getattr__
class Student(object):
    def __init__(self):
        self.name = 'Francis'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr=='age':
            return lambda: 26
        else:
            return 'unknown'
s = Student()
print(s.name)
print(s.score)
print(s.age())
print(s.sex)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

ch = Chain().status.user.list
print(ch)

class Stu(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is %s.' % self.name)

#callable
s = Stu('Francis')
s()
print(callable(s))
print(callable(max))
print(callable([1,2,3]))
print(callable('str'))
