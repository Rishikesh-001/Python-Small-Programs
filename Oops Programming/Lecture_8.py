# <<<<<-----------------------------------------OOP's Programming------------------------------------------------->>>>>

# Make a class of Students and store the name Rishikesh in it
'''
class Student:
    name = "Rishikesh"
    ERP = 606403
    Section = "Section - P3"

s1 = Student()
print(s1.name)
print(s1.ERP)
print(s1.Section)
'''
# Create a class and Object of a Car factory
'''
class Factory:
    colour = "Blue"
    Brand = "Mercedes"

car1 = Factory()
print(car1.Brand)
print(car1.colour)
'''

# Create a class and a constructor for adding students
'''
class Student:
    
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database...")

s1 = Student("Rishikesh") #calling constructor
print(s1.name)

s1 = Student("Amritesh") #calling constructor
print(s1.name)
'''

# Constructor runs automatically upon calling 
'''
class Student:
    def __init__(self):
        print("Constructor running...")

s1 = Student()
'''

# Create a class storing the name and mark of the student
'''
class Student:
    def __init__(self,name,marks): # self is nothing but same as s1 and s2
        self.name = name
        self.marks = marks
        print("Adding details to database...")

s1 = Student("Rishikesh", 96)
print(s1.name, s1.marks)

s2 = Student("Amritesh", 98.9)
print(s2.name, s2.marks)
'''

#<<<-----------------Types of Constructors----------------->>>
'''
# default constructors
def __init__(self):
    pass

# parameterized constructors
def __init__(self,name,marks): # self is nothing but same as s1 and s2
        self.name = name
        self.marks = marks
        print("Adding details to database...")
'''
#<<<------------------------Attributes--------------------------->>>

# Create a class storing the name and mark of the student
'''
class Student:
    college_name = "Rungta College of Engineering and Technology"
    def __init__(self,name,marks): # self is nothing but same as s1 and s2
        self.name = name
        self.marks = marks
        print("Adding details to database...")

s1 = Student("Rishikesh", 96)
print(s1.name, s1.marks)
print(s1.college_name)

s2 = Student("Amritesh", 98.9)
print(s2.name, s2.marks)
print(Student.college_name)
'''

# Create a class storing the nme and marks of the students, set the default name to Anonymous
'''
class Student:
    college_name = "RCET R1"
    name = "anonymous" # class attribute
    def __init__(self,name,marks): 
        self.name = name # object attribute > class attribute
        self.marks = marks
        print("Adding details to database...")

s1 = Student("Rishikesh", 96)
print(s1.name, s1.marks)
print(s1.college_name)

s2 = Student("Amritesh", 98.9)
print(s2.name, s2.marks)
print(Student.college_name)
'''

# create a method to greet students and show their marks
'''
class Student:
    college_name = "RCET R1"
    name = "anonymous" 
    def __init__(self,name,marks): 
        self.name = name 
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)
    
    def get_marks(self):
        return self.marks
        

s1 = Student("Rishikesh", 96)
s1.welcome()
print(s1.get_marks())
'''

# create student class that takes name and marks of 3 subjects as arguements in constructor. Then create a method to print the average
'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "your average score is:", sum/3)

s1 = Student("Rishikesh Raj", [99,90,92])
s1.get_avg()

s2 = Student("Amritesh Raj", [99.97,98])
s2.get_avg()
'''

#<<<----------------------------Static Method------------------------------->>>

# create a method to greet students with "hello"
'''
class Student:
    college_name = "RCET R1"
    @staticmethod # decorator
    def hello():
        print("Hello")

    def __init__(self,name): 
        self.name = name 

    def welcome(self):
        print("welcome student,", self.name)
        

s1 = Student("Rishikesh")
s1.hello()
s1.welcome()
'''

#<<<----------------------------Pillers of OOP's Programming--------------------c---------->>>

# ABSTRACTION: Hiding the implementation details of a class and only showing the essential features to the user.

# ENCAPSULATION: Wrapping data and functions into a single unit (object) 

'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.cluth = True
        self.acc = True
        print("Car Started...")

car1 = Car()
car1.start()
'''

#<<-------------------------------Let's Practice---------------------------------->>

# Create Account class with two attributes - Balance & Account number
# Add 3 methods to debit, credit and print balance

class Account:
    def __init__(self, balance, Acc_num):
        self.bal = balance
        self.acc = Acc_num

    #debit method
    def debit(self,amount):
        self.bal -= amount
        print("Rs.", amount, "was debited.")
        print("total balance =", self.get_balance())

    #credit method
    def credit(self,amount):
        self.bal += amount
        print("Rs.", amount, "was credited.")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.bal
    
acc1 = Account(10000, 335566)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
acc1.debit(10000)