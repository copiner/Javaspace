
#Object Oriented Programming
#Class  Instance
#self
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' %(self.name, self.score))

timmy = Student('Tim Duncan', 90)
timmy.print_score()
