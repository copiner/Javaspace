#__slots__ variable especial
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Francis'
s.age = 25
#s.score = 99

