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

class Student:
    
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database...")

s1 = Student("Rishikesh") #calling constructor
print(s1.name)

s1 = Student("Amritesh") #calling constructor
print(s1.name)



















