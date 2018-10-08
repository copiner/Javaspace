try:
    f = open('app.txt')
    sum = 1 + '1'
    print(f.read())
except OSError as reason:
    print('oserror : ' + str(reason))
except TypeError as reason:
    print('typeerror : ' + str(reason))
finally:
    f.close()

#raise ZeroDivisionError()
