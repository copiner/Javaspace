#Encapsulation
class Turtle:  #Capital
    #attribute
    color = 'red'
    height = 20
    legs = 4
    #method
    def climb(self):
        print('climb enable')
    def eat(self):
        print('eat enable')
    def sleep(self):
        print('sleep...')

tur = Turtle()

print(tur)

tur.climb()
tur.eat()

#inherit list
class Milist(list):
    pass
li = Milist()
li.append(5)
li.append(2)
li.append(7)
print(li)
li.sort()
print(li)
