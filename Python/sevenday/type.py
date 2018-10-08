
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

def fn(self, name='Francis'):
    print('Hi, %s.' % name)

Hi = type('Hi',(object,),dict(hi=fn))
hh = Hi()
hh.hi()
print(type(Hi))
print(type(hh))
