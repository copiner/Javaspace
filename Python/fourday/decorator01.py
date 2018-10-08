#__name__ decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


#now = log(now)

@log
def now():
    print('2016-12-21')

f = now
f()


