def sum(ints):
    ans=ints[0]
    for n in range(1,len(ints)):
        ans+=ints[n]
    return round(ans,2)

def multiply(ints):
    ans=ints[0]
    for n in range(1,len(ints)):
        ans*=ints[n]
    return round(ans,3)

def substraction(ints):
    ans=ints[0]
    for n in range(1,len(ints)):
        ans-=ints[n]
    return round(ans,3)

def division(ints):
    ans=ints[0]
    for n in range(1,len(ints)):
        ans/=ints[n]
    return round(ans,5)

def printMenu():
    '''
    Print Options For Calculations
    '''
    print("What types of Calculations you want to Perform? Type:\n1.  '*' for Multiply\n2. '/' for Division\n3. '+' for Addition\n4. '-' for Substraction:")

def printResult(numbers,optn):
    '''
    Print results
    '''
    if(optn=='*'):
        print(multiply(numbers))
    elif(optn=='/'):
        print(division(numbers))
    elif(optn=='+'):
        print(sum(numbers))
    elif(optn=='-'):
        print(substraction(numbers))
    else:
        print("Error You Entered Wrong Input Run this Code Again!")
        

if __name__ == "__main__":
    '''
    
    '''
    t=int(input("Enter how many times you want to perform the task: "))
    for n in range(0,t):
        c=int(input("How many Numbers you want to take for calculations: "))
        numbers=[]
        for n in range(0,c):
            numbers.append(float(input(f"Enter {n+1} number: ")))
        
        printMenu()
        optn=input()
        printResult(numbers,optn)