# Making a BMI calculator

# User info

user_name = input("Enter your name: ").upper()
user_weight_type = input("Select weight units(i.e 'kg' for Kilogram and 'lb' for Pound): ").lower()
user_weight = float(input("Enter your weight: "))
user_height_type = input("Select unit of height(i.e. 'm' for meter and 'cm' for centimeter): ").lower()
user_height = float(input("Enter your height: "))

# Category list

category_list = [
    [0, 18.5, "Underweight"],
    [18.5, 25, "Healthy"],
    [25, 30, "Overweight"],
    [30, 35, "Obese Class 1"],
    [35, 40, "Obese Class 2"],
    [40, 100, "Obese Class 3"]
]

# Unit conversions

if user_weight_type == "lb":
    converted_weight = (user_weight * 0.453)
else:
    converted_weight = user_weight

if user_height_type == "cm":
    converted_height = user_height/100
else:
    converted_height = user_height

# User BMI

user_bmi = (converted_weight)/(converted_height **2)

# Finding User BMI Category

i = 0
run = True
while run:
    a = category_list[i][0]
    b = category_list[i][1]
    c = category_list[i][2]
    if user_bmi >= a and user_bmi < b:
        user_category = c
        run = False
    i += 1

print(f"Hello {user_name}! Your BMI is {user_bmi} and you fall under catogary of '{user_category}'.")
