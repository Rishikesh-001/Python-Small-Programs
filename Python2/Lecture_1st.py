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
elif(90>=marks>=80):
    print("Congratulation's you have got Grade 'B'")
elif(80>=marks>=70):
    print("Congratulation's you have got Grade 'C'")
elif(70>=marks>=50):
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

#WAP to check if a number is a multiple of 5 or not...


#WAP to enter 2 numbers and print their sum, difference, product and division...

num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2   

print("The sum of the two numbers is ", sum)
print("The difference of the two numbers is ", diff)
print("The product of the two numbers is ", prod)
print("The division of the two numbers is ", div)












