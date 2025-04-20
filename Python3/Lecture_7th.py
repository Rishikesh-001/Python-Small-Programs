#<<<<<------------------------------------File Input/Output in Python-------------------------->>>>>

# import os
# if os.access("demo.txt", os.R_OK):
#     print("You have read access to demo.txt")
# else:
#     print("No read access to demo.txt")


# WAP to read and print the data of the file
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","r")
data = f.read() # reads entire file
print(data)
f.close()
'''
# WAP to read and print only the first line of the file
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","r")
line1 = f.readline() # reads one line at a time
print(line1)
f.close()
'''
# WAP to read and print only the first 10 characters of the file
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","r")
data = f.read(10) # reads only 10 characters of the file including spaces
print(data)
f.close()
'''
# WAP to rewrite the data of the file, with "I am a Coder..."
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","w")
f.write("I am a coder...")
f.close()
'''

# WAP to add more lines to the existing file...
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","a")
f.write("\nThen I will quit the job...")
f.close()
'''

# WAP to delete all the data from the demo.txt file
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","w+")
f.read()
f.write("This is a basic python exercise...")
f.close()
'''

# WAP to write "This is Easy" at the end in the file
'''
f = open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","a+")
f.read()
f.write("\nThis is Easy")
f.close()
'''

#<<<<--------------------------------------With Syntax---------------------------------------->>>>

# WAP to read and print the data from the demo.txt file
'''
with open("C:\\Users\\rishi\\Projects\\Python\\Python3\\demo.txt","r") as f:
    data = f.read()
    print(data)
'''

# WAP to display & erase old data from file, and then add new data to it...
'''
with open("Python3\\demo.txt","r") as f:
    data = f.read()
    print(data)

with open("Python3\\demo.txt","w") as f:
    f.write("new data")
'''

# WAP to add a new file
'''
with open("Python3\\sammple.txt","w") as f:
    f.write("")
'''
# WAP to write How are you doing? in that file
'''
with open("Python3\\sammple.txt","w") as f:
    f.write("how are you doing?")
'''

# WAP to delete file sammple.txt file

import os
os.remove("Python3\\sammple.txt")







