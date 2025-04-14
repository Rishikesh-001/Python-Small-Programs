#DICTIONARY

#Here we will know about dictionary...

'''
dic1 = {
 "name" : "Rishikesh Raj",
 "Class" : "TB05",
 "ERP" : "6606403"

}

print(dic1)

dic2 = {
"name":"Amritesh Raj",
"Class":"TB06",
"ERP":"6606405"
}
print(dic2)
'''

#Adding dictionary with integers, booleans, lists & strings...
'''
student = {
"name":"Amritesh Raj",
"age": 20,
"subjects" : ["Maths","Physics","FOC","Chemistry"],
"CGPA": 9.9,
"Marks":(87,98,56,84),
"is Eligable" : True
}

print(student)
print(type(student))
'''

#To print a specific key or keys from your dictionary...
'''
student = {
"name":"Amritesh Raj",
"age": 20,
"subjects" : ["Maths","Physics","FOC","Chemistry"],
"CGPA": 9.9,
"Marks":(87,98,56,84),
"is Eligable" : True
}

print(student["name"])
print(student["age"])
print(student["CGPA"])
'''

#To assign a new key or change the name from the existing key...
'''
student = {
"name":"Amritesh Raj",
"age": 20,
"subjects" : ["Maths","Physics","FOC","Chemistry"],
"CGPA": 9.9,
"Marks":(87,98,56,84),
"is Eligable" : True
}

student["name"] = "Rishikesh"
student["surname"]="Raj"

print(student)
'''

#Assigning a new key in null dictionary...
'''
null_dict = {}
null_dict["name"] = "Rishikesh Raj"
print(null_dict)
'''

#Making a nested dictionary of a student...
'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}

print(student)
print(student["Subjects"])
'''
#WAP to list all the key elements of our dictionary with no. of keys present...

'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
print(len(student))
print(list(student.keys()))
'''

#WAP to list all the valus of key elements of our dictionary...

'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
print(list(student.values()))
'''

#WAP to list all the keys & its values in tuples...

'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
print(list(student.items()))
'''

#WAP to print individual pair of tuples (key,values)...
'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}

tuples = list(student.items())
print(tuples[0])
print(tuples[1])
'''

#WAP to get the values of the key from dictioary without getting any error... 
'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
print(student["name2"])      #"Error" if input key is wrong 
print(student.get("name2"))   #"None" if input key is wrong
'''

#WAP to add a new key to the dictionary...
'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
student.update({"city":"Chhattisgarh"})
print(student)
'''
#WAP to make a new dictionary add it to earlier dictionary...
'''
student = {
"name" : "Risikesh Raj",
"Subjects" : {
    "maths": 87,
    "physics":96,
    "chemistry": 79
}
}
student1 = {
    "class" : "TB05",
    "ERP":"6606403",
    "city":"Bihar"
}
student.update(student1)
print(student)
'''

#SETS 
#(repeated elements stored only once)
'''
collection = {1,2,3,4,5,"rishikesh","amritesh", 6,4,1,8}

print(collection)
print(type(collection)) #Type of data
print(len(collection))  #Total no. of items
'''

#WAP to print empty set
'''
collection1 = {}      #Empty dictionary
collection2 = set()   #Empty set 

print(type(collection1))
print(type(collection2))
'''

#WAP to add & remove elements from a set...
'''
collection = set()

collection.add(1)
collection.add(1)
collection.add(4)
collection.add("Monkey")
collection.add("Dog")
collection.add(8)
collection.add("Hello")
collection.add("Kitty")
collection.add(87.90)
collection.add((1,2,5,8,3,0,6.8,8)) #we can add a tuple to our set, but not a list (tuples are immutable) 

collection.remove(1)
collection.remove("Dog")

print(collection)
'''
#WAP to clear all the elements of the set...
'''
collection = set()

collection.add(1)
collection.add(1)
collection.add(4)
collection.add("Monkey")
collection.add("Dog")
collection.add(8)
collection.add("Hello")
collection.add("Kitty")
collection.add(87.90)
collection.add((1,2,5,8,3,0,6.8,8))

collection.clear() 
print(len(collection))
'''

#WAP to remove a random element from the set...
'''
collection = {"rishikesh","amritesh",'coding',"python","c++","java"}
collection.pop()
print(collection)

print(collection.pop()) #To print a random element
'''

#WAP to print the union & intersection of 2 sets...
'''
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1.union(set2))        #Union
print(set1.intersection(set2))  #intersection
'''

# PRACTICE QUESTIONS

#WAP to store the following word meanings in a python dictionary
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"
'''
Python_dictionary = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture", "list of facts & figures"),
    
}
print(Python_dictionary)
'''

# You are given a list of subjects for students.
#  Assume one classroom is required for 1 subject. How many classrooms are needed by all students...
# "python","java","C++","python","javascript","java","python","java","C++","C"

'''
students = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(students))
'''

#WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary & add one by one.
#  Use subject name as key & marks as value... 

# 1st way:
'''
a = input(str("Enter Physics marks:"))
b = input(str("Enter chemistry marks:"))
c = input(str("Enter maths marks:"))

marks = {
    "Physics": a,
    "chemistry": b,
    "maths": c
}

print(marks)
'''
#2nd way:
'''
a = float(input("Enter Physics marks:"))
b = float(input("Enter chemistry marks:"))
c = float(input("Enter maths marks:"))

marks = {}

marks.update({"Physics": a})
marks.update({"chemistry": b})
marks.update({"maths": c})

print(marks)
'''

#Figure out a way to store 9 & 9.0 as seperate values in the set...
'''
# 1st method
values = {
    ("float",9.0),
    ("integer",9)
}
print(values)

# 2nd method
values = {9, "9.0"}
print(values)
'''









