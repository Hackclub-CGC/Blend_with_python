a=float(input("Enter 1st Number: "))
b=float(input("Enter 2nd number: "))
c=input("What type calculations you want to do?\n1. Type 'm' for Multiply\n2. Type 'd' for division\n3. Type 'a' for addition\n4. Type 's' for substraction. ")

if(c=='m'):
  print(a*b)
elif(c=='d'):
  print(a/b)
elif(c=='a'):
  print(a+b)
elif(c=='s'):
  print(a-b)
else:
  print (-1)