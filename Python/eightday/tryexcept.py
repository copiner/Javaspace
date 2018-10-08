#try...except...finally
try:
    print('try...')
    #r = 10 / int('a')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError: ', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError: ', e)
else:
    print('no error!')
finally:
    print('finally...')
print('ENd')

#BaseException
def foo():
    pass
def bar():
    pass

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')#the subclass of ValueError inherit BaseException
