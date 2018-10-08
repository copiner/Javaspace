
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

person('Tim', 39)
person('Bob', 35, city='zhejiang')

extra={'city':'beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

