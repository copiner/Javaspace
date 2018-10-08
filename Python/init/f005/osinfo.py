#os
import os
print(os.getcwd())
print(os.listdir())
#os.mkdir("test")
#os.rmdir("test")
print(os.curdir)

#os.path

print(os.path.basename("osinfo.py"))
print(os.path.dirname("E:\\python\\init\\f005\\osinfo.py"))

print(os.path.join("A", "B", "C"))
print(os.path.join("E:\\", "A", "B", "C"))

print(os.path.split('E:\\python\\init\\f005\\osinfo.py'))
print(os.path.splitext('E:\\python\\init\\f005\\osinfo.py'))

print(os.path.getatime('E:\\python\\init\\f005\\osinfo.py'))

ti = os.path.getatime('E:\\python\\init\\f005\\osinfo.py')
import time
print(time.gmtime(ti))
print(time.localtime(ti))

t = os.path.getmtime('E:\\python\\init\\f005\\osinfo.py')
print(time.localtime(t))
