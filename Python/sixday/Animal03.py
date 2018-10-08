
class Animal(object):
    def run(self):
        print('Animal is running..')

class Dog(Animal):
    def run(self):
        print('Dog is runing...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

#add Tortoise
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Tortoise())
#python and java difference
class Timer(object):
    def run(self):
        print('Start..')

run_twice(Timer())
