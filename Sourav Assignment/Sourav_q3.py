#To store user's Email and Date Of Birth

mail=str (input("User please enter your E-mail Adress here"))
dob = str (input("User please enter your Date Of Birth here"))
 
# Let's store the above information
credentials={"E-mail" : mail , "Date of Birth" : dob}

print("These are your credentials according to you")
print(credentials)
print ("Please confirm your credentials")

credentials["E-mail"]=str (input("Please enter the final E-mail Address"))  

print("The Final Credentials are =")
print(credentials)
print("""Thank You Dear User
Have A Nice Day
""")
