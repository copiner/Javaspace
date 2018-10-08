class MiDicriptor:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)
    def __set__(self, instance, value):
        print("setting...", self, instance, value)
    def __delete__(self, instance):
        print("deleting...", self, instance)
class Te:
    x = MiDicriptor()


e = Te()
print(e)
print(Te)

e.x
e.x = 'sth'

del e.x
