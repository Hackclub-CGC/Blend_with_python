#To store user's Email and Date Of Birth

mail=str (input("User please enter your E-mail Adress here"))
dob = str (input("User please enter your Date Of Birth here"))
 
# Let's store the above information
credentials={ "E-mail" : mail , "Date of Birth" : dob}

print("These are your credentials according to you")
print(credentials)
print (""" Please confirm your credentials. 
If you wish to change them please enter "1". 
If you wish to keep the same credentials please enter "0" """)
choice=input("choice")
print(choice)
if(choice==1):
    mail=input("Please enter the modified E-mail Address")
    dob=input("Please enter the modified DOB")
else:
    mail=mail
    dob=dob

credentials[1] = c = str(input("Please enter the final E-mail Address"))  
credentials[0] = d = str(input("Please enter the final Date Of Birth"))

print ("The Final Credentials are =")
print (credentials)
print("""Thank You Dear User
Have A Nice Day
""")
