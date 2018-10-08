
import os
print(os.path.abspath('.'))
#os.path.join('./','francis')
#os.mkdir('./francis/testdir')
#os.path.split()
#os.path.splitext()
#os.rename()
#os.remove()

#shutil copyfile()


l = [x for x in os.listdir(',') if os.path.isdir(x)]
print(list(l))
L = [x for x in os.listdir(',') if os.path.isfile(x) and os.path.split(x)[1]=='.py']
print(list(L))
