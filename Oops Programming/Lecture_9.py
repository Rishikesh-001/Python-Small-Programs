# deleting an object 

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rishikesh Raj")
print(s1.name) # we will get our output
del s1 # s1 or student 1 object is deleted 
print(s1.name) # here we will get error