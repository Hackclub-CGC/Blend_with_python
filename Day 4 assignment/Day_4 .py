"""this calculator performs following functions
Addition
Subtraction
Multiplication
Division
"""
#Let x and y be the two numbers
x=float(input("Enter your first number here"))
y=float(input("Enter your second number here"))

# To Perform addition Enter 1 
# To Perform subtraction Enter 2
# To Perform multiplication Enter 3 
# To Perform division press Enter 4

choice= int(input("Enter refernce no. of your preferred mathematical operation"))

if(choice==1):
    sum=float(x+y)
    print("Addition of the two number gives=")
    print(sum)

elif(choice==2):
    sub=float(x-y)
    print("Subtraction of the two number gives=")
    print(sub)

elif(choice==3):
    mult=float(x*y)     
    print("Multiplication of the two number gives=")
    print(mult)

elif(choice==4):
    div=float(x/y)
    print("Division of the two number gives=")
    print(div)

else:
    print("No such operation defined : Sorry!!!")

print("""Thank You Dear User
Have A Nice Day
""")