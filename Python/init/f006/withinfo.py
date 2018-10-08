try:
    f = open('data.txt', 'w')
    for line in f:
        print(line)
except OSError as reason:
    print('error : ' + str(reason))
finally:
    f.close()#pos exi err

try:
    with open('data.txt', 'w') as f:
        for line in f:
            print(line)
except OSError as reason:
    print('error : ' + str(reason))


