# we need to solve the problem by making a dictionary of the emails and dobs 

a = str (input("please enter your email address here"))
b = str( input ("please enter your date of birth "))

i = { "email" : a , "dob" : b}

print ("these are the credentials according to your input")
print (i) 
print (""" please confirm your credentials below . if you wish to change them please enter the desired input. If you wish to keep the same please enter the same value """)

i["email"] = c = str(input("please enter the final email address"))
i["dob"] = d = str(input("please enter the final date of birth"))

print ("the final credentials are :-")
print (i)