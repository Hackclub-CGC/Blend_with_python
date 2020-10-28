def Sum(a,b):
    return a+b
def Product(a,b):
    return a*b
def difference(a,b):
    return a-b
def reminder(a,b):
    return a%b

if __name__ == "__main__":
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))

    print(f"Sum of {a} and {b} is {round(Sum(a,b),2)}")
    print(f"Product of {a} and {b} is {round(Product(a,b),2)}")
    print(f"Difference of {a} and {b} is {round(abs(difference(a,b)),2)}")
    print(f"Reminder of {a} and {b} is {round(reminder(a,b),2)}")