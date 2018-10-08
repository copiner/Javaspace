
class Student(object):
    pass

s = Student()
s.name = 'Francis'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
ss = Student()
#ss.set_age(20)

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)
ss.set_score(99)
print(ss.score)
