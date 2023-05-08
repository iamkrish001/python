a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("add       : 1")
print("subtract  : 2")
print("multiply  : 3")
print("divide    : 4")

operation = int(input("Select a  number from 1 to 4 "))
while True:
    if(operation == 1):
        print("The sum is  ", a+b)
    elif(operation == 2):
        print("The difference is  ", a-b)
    elif(operation == 3):
         print("The product  is  ", a*b)
    elif(operation == 4):
         print("The quotient is  ", a/b)
         break 
    if(operation != 1 or 2 or 3 or 4):
        operation = int(input("Please select a  number from 1 to 4 "))
    
