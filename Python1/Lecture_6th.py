#<<<<----------------------Lecture 6 is all about Functions and Recursion----------------------->>>>

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

'''
print(calc_diff(10,8)) # we can also leave arguement value, if we have default values
print(calc_diff())
'''

# <<<-----------------Practice Questions----------------->>>

# WAF to print the length of a list (list is the parameter)
'''
nums = [1,5,9,7,3,6,4,8,2]
cities = ["Patna","Delhi","mumbai","noida","bilai","Raipur"]

def calc_len(list):
    return len(list)

print(calc_len(nums))
print(calc_len(cities))
'''

# WAF to print all the elements of the list on a sigle line(list is a parameter)

nums = [1,5,9,7,3,6,4,8,2]
cities = ["Patna","Delhi","mumbai","noida","bilai","Raipur"]
heros = ["Ironman","Thor","Hulk","Batman","Black Panther","Captain America"]

def print_list(list):
    for element in list:
        print(element, end=" ")
'''
print(print_list(cities))
'''
'''
def print_ele(list):
    return str(list)

print(print_ele(cities))
print(print_ele(nums))
print(print_ele(heros))
'''

# WAF to print all the elements of the list on a different lines (list is a parameter)
'''
nums = [1,5,9,7,3,6,4,8,2]
cities = ["Patna","Delhi","mumbai","noida","bilai","Raipur"]
heros = ["Ironman","Thor","Hulk","Batman","Black Panther","Captain America"]

def print_list(list):
    for element in list:
        print(element, end="\n")

print(print_list(cities))
'''

# WAF to find the factorial of n

def fact_num(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

'''
k = int(input("Enter number to find Factorial:"))
print(fact_num(k))
'''

# WAF to convert USD in INR

def converter(usd_val):
    inr_val = usd_val * 85.39
    print(usd_val, "USD =", inr_val, "INR") 
'''
l = float(input("Enter USD to convert in INR:"))
converter(l)
'''

# WAF to find if the input number is odd or even

def check_num(number):
    if((number % 2) == 0):
        print("EVEN")
    else: print("ODD")

l = int(input("Enter your number:"))
check_num(l)











