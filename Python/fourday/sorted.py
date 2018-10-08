
#sorted
L = [32,-12,-5,9,21]
print(list(sorted(L)))

s = sorted(L, key=abs)
print(list(s))

L = ['bobo','Tim','Parker','manu']
s = sorted(L, key=str.lower)
print(list(s))
s = sorted(L, key=str.lower, reverse=True)
print(list(s))

from operator import itemgetter
students = [('bobo',100),('tim',90),('manu', 88),('parker',86)]
stu = sorted(students, key=itemgetter(0))
print(list(stu))

