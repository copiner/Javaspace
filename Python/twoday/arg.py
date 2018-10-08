
#arguments
def power(x, n):
    m = 1
    while n>0:
        n=n-1
        m=m*x
    return m

print(power(5, 2))
print(power(5, 3))

def info(name, gender, age=6, city='zhejiang'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)

info('Sarah', 'F')
info('Bob', 'M', 7)
info('Tim', 'M', city='beijing')
