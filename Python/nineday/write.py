
f = open('about.txt','w')
f.write('Good morning')
f.close()

with open('about.txt','w') as f:
    f.write('Good Night')
