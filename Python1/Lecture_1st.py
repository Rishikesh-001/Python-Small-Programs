#Program to find if the string is ending with the letters give by us... 
'''
str = "I am a great Player of Badminton"
print(str.endswith("ton"))
'''
# Program to capatilize first letter of the string.
'''
str = "i am a great Player of Badminton"
print(str.capitalize())
'''
# Program to replace the words from the string

'''
str = "I don't know why I am here, but I know I am here because My mind told me"
print(str.replace("know","yeah"))
'''

# Program to print only specific part of the given string...
'''
str = "Call the boy, Named ISHAAN"
print(str[5:13])
'''
# Program to find a word or letter or character in the given string...
# This function will find the character and tell us the character's index...

'''
str = "I don't know why I am here, but I know I am here because My mind told me"
print(str.find("know"))
'''
# Program to count any word or character...
'''
str = "I don't know why I am here, but I know I am here because My mind told me"
print(str.count("know"))
'''

# WAP to input users first name and print its length...
'''
a = str(input("Enter your first name:"))
print("length of your name is", len(a))
'''
# WAP to count number of occurance of a's in a string from input...
'''
a = str(input("Enter any thing, we will count the number of time's A is present:"))
print(a.count("a"))
'''

# WAP using coditional statements...

'''
age = int(input("Enter your age:"))
if(age>=18):
    print("You are eligible to vote")
else :
    print("You are under age")
'''

# WAP to tell the people's about the Traffic Signal LIght...
'''
str = input("Enter the Traffic Signal:")
if (str == "Green"):
    print("You can go now")
elif (str == "Yellow"):
    print("wait, look around")
elif (str == "Red"):
    print("Stop!") 
else: print("The light is broken")
'''

# WAP to assign grades to the students on the basis of Marks...
'''
marks = float(input("Enter your marks:"))
if (marks>=90):
    print("Congratulation's you have got Grade 'A'")
elif(90>marks>=80):
    print("Congratulation's you have got Grade 'B'")
elif(80>marks>=70):
    print("Congratulation's you have got Grade 'C'")
elif(70>marks>=50):
    print("Congratulation's you have got Grade'D'")
else: 
    print("You are Fail")
'''

# WAP using nesting of conditionl statements...

'''
age = int(input("Enter your age:"))
if(age>=18):
    if(age>=70):
        print("Cannot Drive")
    else: print("Can Drive")
else:
    print("Cannot Drive")
'''

# WAP to check if a number entered by the user is odd or even...
'''
a = int(input("Enter the Number:"))
if((a%2) == 0):
    print("even")
else: print("Odd")
'''

# WAP to find the greatest of 3 numbers entered by the user...

'''
a = float(input("Eter 1st number:"))
b = float(input("Eter 2nd number:"))
c = float(input("Eter 3rd number:"))

if (a>=b) and (a>=c):
    print("The Greatest number is ", a)
elif (b>=a) and (b>=c):
    print("The Greatest number is ", b)
elif (c>=a) and (c>=b):
    print("The Greatest number is ", c)
else:
    print("The entered number is Printed")
'''

# WAP to check if a number is a multiple of 7 or not...
'''
a = int(input("Enter the number:"))
if ((a%7)==0):
    print("Hence, it is multiple of 7")
else:
    print("It is not a multiple of 7")
'''


#WAP to find the area of a circle...
'''
R = float(input("Enter the radius of circle:"))
area = 3.14 * R * R
print("Area of Circle is: ", area)
'''
#WAP to find the area of a triangle...
'''
Side = float(input("Enter the side of the triangle:"))
height = float(input("Enter trhe height of the triangle:"))
area = (Side * height) / 2
print("Area of triangle is: ", area)
'''

# Program to compute the sum of all natural numbers from 1 to n
'''
n = int(input("Enter a non-negative integer n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    total_sum = n * (n + 1) // 2  # Using the formula for the sum of the first n natural numbers
    print(f"The sum of all natural numbers from 1 to {n} is: {total_sum}")
'''
'''
n = int(input("Enter a non-negative integer n: "))

if 1 <= n <= 10000 and n < 0:
    print("Please enter a non-negative integer.")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print(f"The sum of all natural numbers from 1 to {n} is: {total_sum}")
'''

#WAP to input users first name and print its length...
'''
name = str(input("Enter your first name:"))
print(len(name))
'''
#WAP to cout occurance of $ in a string...
'''
string = str(input("Enter any thing, we will count the number of time's $ is present:"))
print(string.count("$"))
'''










