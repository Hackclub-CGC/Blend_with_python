"""This is a BMI calculator
"""
print("This is a BMI calculator")
name=str(input("Enter your name: "))
mass=int(input("Enter your weight in kg's"))
height=float(input("Enter your height in meters!"))
BMI=mass/(height*height)
print(f'Hey {name},your height is {height}, your weihgt is:{mass}and your BMI is {BMI} ')

