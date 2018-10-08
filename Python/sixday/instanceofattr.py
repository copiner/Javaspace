
class Student(object):
    name = 'cookie'

s = Student()
print(s.name)
print(Student.name)

s.name = 'Calvin'
print(s.name)
print(Student.name)

del s.name
print(s.name)

