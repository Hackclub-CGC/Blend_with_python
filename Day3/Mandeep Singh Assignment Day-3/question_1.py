# Defineing functions 

def Sum(a,b):
    return a+b

def Product(a,b):
    return a*b

def difference(a,b):
    return a-b

def reminder(a,b):
    return a%b

# Taking input from user

a = float(input("Enter  your first number: "))
b = float(input("Enter your second number: "))

print( 
"""
    Enter 'add' for addition of both number
    Enter 'sub' for subtraction of both number
    Enter 'mul' for multiplication of both number
    Enter 'rem' to get remainder of number on division
    Enter 'all' to display all the above resuls
"""
)

user_choice = input("Enter your choise here: ").lower()

# Displaying text according to user's choice

if user_choice == 'add':
    print(f"Sum of {a} and {b} is {round(Sum(a,b),4)}")

if user_choice == 'sub':
    print(f"Difference of {a} and {b} is {round(abs(difference(a,b)),4)}")

if user_choice == 'mul':
    print(f"Product of {a} and {b} is {round(Product(a,b),4)}")

if user_choice == 'rem':
    print(f"Reminder of {a} and {b} is {round(reminder(a,b),4)}")

if user_choice == 'all':
    print(f"Sum of {a} and {b} is {round(Sum(a,b),4)}")
    print(f"Difference of {a} and {b} is {round(abs(difference(a,b)),4)}")
    print(f"Product of {a} and {b} is {round(Product(a,b),4)}")
    print(f"Reminder of {a} and {b} is {round(reminder(a,b),4)}")
