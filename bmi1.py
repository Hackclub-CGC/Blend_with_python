#This is a BMI calculator
print("This is a BMI calculator")
name=str(input("enter your name"))
mass=int(input("enter your weight in kg's"))
height=float(input("enter your height in meters!"))
bmi=mass/(height*height)
print(f'Hey {name},your height is {height},your weight is {mass} and your BMI is {bmi}')
