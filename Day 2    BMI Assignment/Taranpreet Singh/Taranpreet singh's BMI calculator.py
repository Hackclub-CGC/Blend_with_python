# This is BMI calculator made by Taranpreet Singh
# input to be entered here
name=input("Please enter your good name : ")
sex=input("Your sex :")
age=int(input(f"Hello,{name} Please enter your age :"))
print(f"\n{name.upper()},\n     IF you know your weight in \"POUND\" than press :1\n       if you know your weight in \"KG\" than press :2 ")
weightType=int(input(":"))
if weightType ==1:
    weight=float(input(f"Enter your weight in Pound : "))
    weight*=.454
elif weightType ==2:
    weight=float(input(f"Enter your weight in KILOGRAM : "))
else:
    print("choose a right option ,Please try again")
    # declare height:
print(f"\n\n{name.upper()},\n    IF you know your height in \"METRE\" than press :1\n    if you know your height in \"FOOT\" than press :2 ")
heightType=int(input(":"))
if heightType == 1:
    height=float(input(f"Enter your height in Metre : "))
elif heightType == 2:
    height=float(input(f"Enter your height in Foot : "))
    height*=.30
else:
    print("choose a right option ,Please try again")

# Result
bmi=weight/height**2
if 18.5 < bmi <25:
    print(f"\n BMI report \n Name:{name},\n  Age: {age}\n sex: {sex} \n Your BMI is {bmi} \n You are 'HEALTHY WEIGHT';\n keep it up!")
elif 25<bmi<=40:
    print(f"\n BMI report \n Name:{name},\n  Age: {age}\n sex: {sex} \n Your BMI is {bmi} \n You are 'OVERWEIGHT' ; \n You need to decrease your daily Diet, and exercise daily to stay fit.")
elif bmi<18:
    print(f"\n BMI report \n Name:{name},\n  Age: {age}\n sex: {sex} \n Your BMI is {bmi} \n You are 'UNDERWEIGHT' ; \n You need to take healthy Diet.")
elif bmi>=40:
    print(f"\n BMI report \n Name:{name},\n  Age: {age}\n sex: {sex} \n Your BMI is {bmi} \n You are 'MORBIDLY OBESED' ;\n You need to DECREASE your daily Deight, and exercise daily in order to be fit, and even you should consult a health expert.")
else:
    print("wrong entry")



print("\n                  \"STAY FIT AND HEALTHY, LIVE A CHEERFUL LIFE\"  ")
#End of code