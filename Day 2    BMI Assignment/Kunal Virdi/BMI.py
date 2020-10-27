#THIS IS A BMI CALCULATOR
print("Welcome to BMI Calculator")
Name= str(input("Enter Your Name: "))

mass = int(input("Enter Your Weight in KG: "))

height = float(input("Enter Your Height in Feets: "))
height/=3.2808 #convert height into meters

# Formula Starts Here

Bmi =  mass/(height*height)

print(f"Hey {Name}, Your height is {round(height,2)}M , Your weight is {mass}KG, Your BMI is {round(Bmi,2)}")