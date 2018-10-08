
try:
    #print(int('a'))
    print(int('2'))
except ValueError as reason:
    print('error : ' + str(reason))
else:
    print('no error')
