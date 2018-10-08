
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('francis', 19, 76)
#print(json.dumps(s))# TypeError

def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
d = json.dumps(s, default=student2dict)
print(d)

a = json.dumps(s, default=lambda obj: obj.__dict__)
print(a)

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"name":"Calvin","age":20,"score":76}'
jso = json.loads(json_str, object_hook=dict2student)
print(jso)

