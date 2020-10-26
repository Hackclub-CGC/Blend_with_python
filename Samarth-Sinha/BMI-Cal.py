#BMI CALCULATOR

print("HEY I AM BMI CALCULATOR \n")

Name = str(input("Enter Your Amazing Name -  "))
print(f"Hey {Name}\n")
mass = int(input("Enter Your Body Mass - "))
height = float(input("Enter Your Height - "))

#Calculate The BMI 

BMI = mass/(height*height);

# Result 
print(f"Your BMI IS {BMI}" )
