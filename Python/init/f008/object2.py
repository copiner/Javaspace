#polymorphism
class Anna:
    def fun(self):
        print('Anna coming..')

class Francis:
    def fun(self):
        print('Francis coming...')

a = Anna()
b = Francis()
a.fun()
b.fun()

