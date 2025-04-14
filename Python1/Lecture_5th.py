#Loops in Python

#WAP to print "Hello World" 10 times...
'''
i = 1
while i <= 5:
    print("Hello")
    i = i + 1

print(i)
'''
# Printing Rishikesh Raj 10 times with its count...
'''
count = 1
while count <= 10:
    print("Rishikesh Raj", count)
    count = count + 1

print(count)
'''
#WAP to print numbers from 1-100
'''
i = 1
while i <=100:
    print(i)
    i += 1

print("Loop Ended")
'''
# WAP to print numbers from 88-1
'''
i = 88
while i>=1:
    print(i)
    i -= 1

print("Loop Ended")
'''

# Writing a infinite loop
'''
i = 5
while i < 6:
    print(i)
    i -= 1

print ("Loop Ended")
'''

# Print numbers from 1-100 
'''
i = 1
while i<= 100:
    print(i)
    i = i + 1
    
print("Loop Ended")

'''
# WAP to print numbers from 100 - 1
'''
i = 100
while i>0:
    print(i)
    i = i - 1
'''

# WAP to print the multiplication table of number n
'''
n = int(input("Enter the number:"))
i = 1
while i <= 10:
    print(n*i)
    i = i + 1
   
print("Loop Ended")
'''

# Print the elements of the following list using a loop...
# [1,4,9,16,25,36,49,64,81,100]

'''
list = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1
'''
# Another method
'''
i = 1
while i <= 10:
    print(i*i)
    i += 1
'''
# Search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)
'''
l = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(l):
    
    if (l(i) == x):
      print("FOUND at index:", i)
    i = i + 1
'''




















