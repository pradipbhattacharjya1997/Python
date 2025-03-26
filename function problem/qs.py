# 1. Write a function to find maximum of three numbers in Python.

def maximum_num (val1,val2,val3):
    if val1 > val2 and val1 > val3:
        print(val1,"is the greatest number")
    elif val2 > val1 and val2 > val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")


maximum_num(45,3,46)

# 2. Write a Python function to create and print a list where the values
# are square of numbers between 1 and 30.

def create_list():
    l =[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())

# 3. Write a Python function that takes a number as a parameter and
# check if the number is prime or not.

def check_prime(num):
    if num == 1:
        print("it is not a prime number")
    if num == 2:
        print("it is a prime number")
    if num > 2 :   
       for i in range (2, num):
        if num % i == 0:
            print("it is not a prime number")   
            break

    else:
        print("it is a prime number")

check_prime(13)

# 4. Write a Python function to sum all the numbers in a list.

def add(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return(total)

print(add([12,4,5,6,7,8]))

# 5. Write a Python program to solve the Fibonacci Sequen
# Recursion.
def fs(num):
    if num == 1:
        return (0)
    elif num == 2:
        return(1)
    else:
        return (fs(num-1)+fs(num-2))

print(fs(7))