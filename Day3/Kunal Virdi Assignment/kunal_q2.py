def list(n):
    lst=[]
    for x in range(0,n):
        elements = input(f"Enter {x+1} element: ")
        lst.append(elements)
    print(lst)
if __name__ == "__main__":
    n = int(input("Enter number of elements you want to store in list:"))
    while(n<3):
        n=int(input("Please Enter Elements more than or equals to 3: "))
    list(n)




        

