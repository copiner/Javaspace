
f = open('readme.txt', 'r')

for line in f.readlines():
    print(line.strip())


f = open('xiao.jpg', 'rb')
f.read()

f = open('xiao.jpg','r', encoding='gbk', errors='ignore')
