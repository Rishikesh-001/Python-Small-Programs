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

#-----------------------------------------------------New Lecture--------------------------------------------------------------

#WAP to print numbers from 1 to 10
'''
i = 1
while i <= 10:
    print(i)
    i += 1
'''

#WAP to print 9 100 times along with its serial number
'''
i = 1
while i <= 100:
    print(i, ":", 9)
    
    i += 1 
print("Loop Ended")
'''

#WAP to print numbers from 100 to 1
'''
i = 100
while i>= 1:
    print(i)
    i -= 1
print("Loop Ended")
'''
#WAP to print all the numbers less than 10 (Infinite loop)
'''
i = 10
while i <= 11:
    print(i)
    i -= 1
'''

#Print the multiplication table of a number N
'''
Number = int(input("Enter the Number:"))
i = 1
while i <= 10:
    print(Number*i)
    i += 1
'''

#Print the elements of the following list using loop [1,4,9,16,25,36,49,64,81,100]
'''
i = 1
while i <= 10:
    print(i*i)
    i += 1
'''
'''
list = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(list):
    print(list[index])
    index += 1
'''

# WAP to print all the names from the list ["Iron Man","Thor","Hulk,"Black Widow","Captain America","Hawkeye"]
'''
Avengers = ["Iron Man","Thor","Hulk","Black Widow","Captain America","Hawkeye"]
i = 0
while i < len(Avengers):
    print(Avengers[i])
    i += 1
'''
# Search for a number X in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
'''
X = 36
series = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(series):
    if( series [i]  == X):
        print("Found 'X' at index:",i)
    i += 1
'''
# WAP to find a number x occuring first time in the list.  [1,5,6,6,5,4,8,2,3,4,7,9,9,5,4,1,2,3,6,6,9,8,7,4,1,2] 
'''
X = 7
List = [1,5,6,6,5,4,8,2,3,4,7,9,9,5,4,1,2,3,6,6,9,8,7,4,1,2] 
i = 0
while i < len(List):
    if(List[i]==X):
        print("Found the number at Index:", i)
        break #stoppig loop
    else: print("Finding...")
    i += 1
print("End Of Loop")
'''

# WAP to write all the numbers from 1 to 10, skipping 3 & 7
'''
i = 1
while i <= 10:
    if(i==3):
        i += 1
        continue #skip
    elif(i==7):
        i += 1
        continue #skip
    print(i)
    i += 1
'''

# WAP to write all the odd numbers from 1 to 50
'''
i = 0
while i <= 50:
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1
'''

# WAP to write all the even numbers from 1 to 50
'''
i = 0
while i <= 50:
    if(i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i += 1
'''

# WAP to print the names of fruits from the list using FOR loop
'''
Fruits = ["Apple","PineApple","Guava","Grapes","Orange","Banana"]

for names in Fruits:
    print(names)
'''

# WAP to write all the letters of the word "Mitochondria"
'''
str = "Mitochondria"

for letters in str:
    print(letters)
else:
    print("End")
'''

# WAP to write the letters of the word "Mitochondria" only till "d"
'''
str = "Mitochondria"

for Letters in str:
    if(Letters == 'd'):
        print("d Found")
        break
    print(Letters)
else: print("End")
'''

# Print the elements of the list using FOR loop [1,4,9,16,25,36,49,64,81,100]
'''
list = [1,4,9,16,25,36,49,64,81,100]

for indexes in list:
    print(indexes)
'''

# Search for a number X in this tuple using FOR loop [1,4,9,16,25,36,49,64,81,100]
'''
X = 49
list = (1,4,9,16,25,36,49,64,81,100,49)

index = 0
for indexes in list:
    if(indexes == X):
        print("Found at index:", index)
    index += 1
else:
    print("Loop Ended")
'''

# Playing with range
'''
for i in range(5): #range(stop)
    print(i)

for i in range(1,5): #range(start,stop)
    print(i)

for i in range(0,20,2): #range(start,stop,steps)
    print(i)
'''

# Print all the even numbers from 1-100
'''
for i in range(0,101,2):
    print(i)
'''










