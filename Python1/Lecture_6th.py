#<<<<-------------------------------------Lecture 6 is all about Functions and Recursion------------------------------------>>>>

# Write a function to find average of 3 numbers

def calc_avg(a,b,c):
    avg = (a+b+c)/3
    # print(avg)
    return avg
'''
#Find average of 15,20,25
calc_avg(15,20,25)

#Find average of 10,10,10
calc_avg(10,10,10)
'''
'''
# Write a function to find average of 3 numbers by taking input from the user

l = int(input("Enter 1st number:"))
m = int(input("Enter 2nd number:"))
n = int(input("Enter 3rd number:"))
print(calc_avg(l,m,n))
'''

# Write a function to find sum of three numbers

def calc_sum(a,b,c):
    sum = a + b + c
    return sum
'''
print(calc_sum(5,10,20))
'''
'''
# Write a function to find sum of 3 numbers by taking input from the user

l = int(input("Enter 1st number:"))
m = int(input("Enter 2nd number:"))
n = int(input("Enter 3rd number:"))
print(calc_sum(l,m,n))
'''

# Write a function to find Product of two numbers

def calc_prod(a,b):
    product = a * b
    return product
'''
print(calc_prod(5,6))
'''
'''
# Write a fuction to find prodcut of two numbers by taking input from the user
def calc_prod(a,b):
    return a * b

l = int(input("Enter 1st number:"))
m = int(input("Enter 2nd number:"))
print(calc_prod(l,m))
'''

# Write a function to find difference of two numbers (add default values as 1)

def calc_diff( a=1 ,b=1 ):
    return a - b 

print(calc_diff(10,8))
print(calc_diff())

