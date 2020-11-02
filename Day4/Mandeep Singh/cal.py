# MAKING CALCULATOR USING PYTHON

def decorator(x):
    print(x * 100)

decorator("x")
print("To get help enter 'help' in 'choice' option.")
decorator("x")

def help():
    print("""
To start with calculation enter "start" in "choice" option.
To see the last claculate answer enter "last_answer" in "choice" option.
To take last answer as your first number enter "answer" in "choice" option.
To quit the code write "quit" in "choice" option.
""")

telly = 0
run = True
run2 = False

while run:
    user_init = input("Enter your choice: ")

    if user_init == "help":
        help()

    if user_init == "quit":
        print("You have exit the code. Have a nice day. ")
        #run = False
        break

    if user_init == "start":
        telly = 0
        decorator("=")
        user_input = int(input("Enter your number:                                                          "))
        telly = user_input
        run2 = True

    if user_init == "answer":
        user_input = telly
        run2 = True

    if user_init == "last_answer":
        print(f"The answer of the last calculation is '{telly}'.")
        decorator("*")

    while run2:
        user_operator = input("Enter your operator (e.g. '+', '-', '*', '/') or enter '=' to see answer: ")

        if user_operator == "=":
            decorator("=")
            print(f"The answer of the calculation is   '{round(telly, 4)}'.")
            decorator("=")
            run2 = False
        else:
            user_input = int(input("Enter your  next number:                                                    "))

        if user_operator == "+":
            telly += user_input  
    
        if user_operator == "-":
            telly -= user_input

        if user_operator == "/":
            telly /= user_input
            
        if user_operator == "*":
            telly *=  user_input
