# deleting an object 
'''
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rishikesh Raj")
print(s1.name) # we will get our output
del s1 # s1 or student 1 object is deleted 
print(s1.name) # here we will get error
'''

# Private attributes: These are meant to be used only within the class and are not accessible from outside the class...

# create a class with Private attribute
'''
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # add 2 underscore in self.acc_pass to make it private

acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.__acc_pass) # it will give error
'''
# create a class which can access private attributes
'''
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
'''

#<<<----------------------------------Inheritance------------------------------------>>>

# Inheritace in classes: When one class (child/derived) derives the properties & methods of another class(parent/base)

class Car:
    color = "violet"
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fotuner")
car2 = ToyotaCar("Camry")

print(car1.name)
print(car1.start())
print(car1.stop())
print(car1.color)

