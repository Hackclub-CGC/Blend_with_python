"""
we need to create a calculator with basic mathematical operations
the calculator should perform multiplicaton , addition , division and subtraction 
we also need to give the user the choice to make the four of these functions 
"""
print("Hi!, welcome to basic calculator")

#input
a = float(input("Enter The First Number"))
b = float(input("Enter The Second Number"))

#operations 
ad = a + b
m = a*b
d = a/b
s = a-b

#operations input 
i =  int(input("input the operation you want type 1 to add ,  type 2 to multiply , type 3 to subtract , type 4 to divide "))

print("------" * 25)
print("**" * 40)

print( "this is your desired result " ) 

#result 
if i == 1  :
    print(ad)
elif i == 2 :
    print(m)
elif i== 3 :
    print(s)
elif i== 4:
    print(d)
else :
    print("please input the correct operation number ")








