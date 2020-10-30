"""this is a bmi calculator"""
print("this is a bmi calculator")
name=str(input("enter your name"))
mass=int(input("enter your weight in kg's"))
height=float(input("enter your height in meters"))
bmi=mass/(height*height)
print(f'hey {name},your heightis {height},yourweight is {mass} and your BMI is {bmi}')