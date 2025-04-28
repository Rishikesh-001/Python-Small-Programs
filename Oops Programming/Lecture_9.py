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

'''
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
'''

# TYPES OF INHERITANCE - Single Level Inheritance

'''
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
'''

# TYPES OF INHERITANCE - Multi Level Inheritance

'''
class Car:
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.start())
'''

# TYPES OF INHERITANCE - Multiple Inheritance
'''
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
'''

# Super method for calling Constructors...
'''
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        super().start()
        self.name = name

car1 = ToyotaCar("Camry","Electric")
print(car1.type)
'''

# Class Method: A class method is bound to the class & receives the class as an implicit first arguement
#Note: Static method can't access or modify class state and generally for utility
'''
class Person:
    name = "anonymous"

    def change_name(self,name):
        self.name = name

p1 = Person()
p1.change_name("Khushi Mahato")
print(p1.name)
print(Person.name)
'''
# or
'''
class Person:
    name = "anonymous"

    def change_name(self,name):
        Person.name = name

p1 = Person()
p1.change_name("Khushi Mahato")
print(p1.name)
print(Person.name)
'''
# or
'''
class Person:
    name = "anonymous"

    def change_name(self,name):
        self.__class__.name = "Khushi"

p1 = Person()
p1.change_name("Khushi Mahato")
print(p1.name)
print(Person.name)
'''
# class method
'''
class Person:
    name = "anonymous"

    # def change_name(self,name):
    #     self.__class__.name = "Khushi"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Khushi Mahato")
print(p1.name)
print(Person.name)
'''

# Property decorator

# Write a program to display the percentage of marks of the student
'''
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student(97,98,99)
print(stu1.percentage)

stu1.phy = 86 # Updating value of physics
print(stu1.phy)
print(stu1.percentage) # Percentage is still the same (Problem)
'''

# Using Property decorator
'''
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student(97,98,99)
print(stu1.percentage)

stu1.phy = 86 # Updating value of physics
print(stu1.percentage) 
'''


#<<<----------------------------------------POLYMORPHISM------------------------------------------>>>

# Polymorphism: Operator Overloading
# When the same operator is allowed to have different meaning according to the context

# for examople:
'''
print(1 + 2) #3
print(type(1))

print("apna" + "college") #apnacollege
print(type("apna"))

print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6]
print(type([1,2,3]))
'''
# Create a class for complex numbers
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()
'''
# Create an addition logic for Complex numbers
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def add(self, num2):
        newreal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newreal, newImg)


num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

# num3 = num1 + num2  # Error for Unsupported Operand type
# num3.showNumber() 
'''

# Solving the error with Dunder function, Dunder function is nothing but when we add double underscores before the operators, it becomes dunder function...

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2): # converted add to dunder function
        newreal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newreal, newImg)


num1 = Complex(1,2)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()



