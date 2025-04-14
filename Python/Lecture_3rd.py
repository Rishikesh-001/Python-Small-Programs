# WAP to slice a given list in the program...
'''
marks = [88,90,76,7,20,61,36]
print(marks[1:4])
'''
# WAP to add a number in the existing list & then sort it in assending order...
'''
marks = [88,90,76,7,20,61,36]
marks.append(97)
marks.sort()
print(marks)
'''
# Pritning the previous list in decending order...
'''
marks = [88,90,76,7,20,61,36]
marks.append(97)
marks.sort(reverse=True)
print(marks)
'''
# Strings can also be sorted in alphabetical order...
'''
alphabets = ["c","k","f","d","s","a"]
alphabets.sort()
print(alphabets)
'''

# Reversing the entire list...
'''
alphabets = ["c","k","f","d","s","a"]
alphabets.reverse()
print(alphabets)
'''

# Adding "H" in between f & d in the previous list...
'''
alphabets = ["c","k","f","d","s","a"]
alphabets.insert(3,"H")
print(alphabets)
''' 

# Removing a specific element from list...
'''
alphabets = ["c","k","f","d","s","a"]
alphabets.pop(4)
print(alphabets)
'''

# WAP to ask the user to enter the names of their 3 favorite movies & store them in a list...
'''
a = str(input("Enter your 1st favorite movie:"))
b = str(input("Enter your 2nd favorite movie:"))
c = str(input("Enter your 3rd favorite movie:"))

print(list[a,b,c])
'''
'''
movies = []
mov1 = input("Enter your 1st favorite movie:")
mov2 = input("Enter your 2nd favorite movie:")
mov3 = input("Enter your 3rd favorite movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
'''


# WAP to check if a list contains a palindrome of elements
'''
list1 = [1,2,3,4,5,4,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#WAP to ask the user troi enter the 3 names of their favorite movies and store them in a list...
'''
a = input(str("Enter name of 1st movie: "))
b = input(str("Enter name of 2nd movie: "))
c = input(str("Enter name of 3rd movie: "))

list = [a,b,c]
print(list)
'''







