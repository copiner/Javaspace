
#Object Oriented Programming
#Class  Instance
#self
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' %(self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
timmy = Student('Tim Duncan', 90)
#print(timmy.__name)
#print(timmy.__score)
print(timmy.get_name())
print(timmy.get_score())

parker = Student('Tony parker',80)
parker.set_score(120)
