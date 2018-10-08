
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name: ', name, 'age: ', age, 'other: ', kw)

person('Jack',24,city='Beijing', addr='zhejiang',code=10110)

#keywords function
def per(name, age, *, city='hangzhou', job):
    print(name, age, city, job)

per('Jack',24,city='Beijing', job='art')
per('Jack',24,job='art')

def pe(name, age, *arg, city, job):
    print(name, age, city, job)

pe('Jack',24,city='Beijing', job='Art')
