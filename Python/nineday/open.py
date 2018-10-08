#open
try:
    f = open('readme.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('readme.txt', 'r') as f: #don't call f.close()
    print(f.read())

