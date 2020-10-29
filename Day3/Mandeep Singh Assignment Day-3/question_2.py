
data = []

# Taking number of elements in a list as input

while True:
    num_of_element = int(input("Enter number of elements you want to add to list: "))
    if num_of_element < 3:
        print("Need atleast 3 elements")
    else:
        print("*" * 100) # Decorator
        break

# Adding elements to list with their correst type

i = 0
while i < num_of_element: 
    element = input("Enter your element here: ")
    if i<1:
        print("Enter type as 'str' for string, 'int' for integer, 'bool'for boolean and 'float' for floating point number")
    element_type = input("Enter type of element you entered: ")

    print("=" * 100) # Decorator

    # Converting element to its ture type

    if element_type == 'int':
        converted_element = int(element)
    elif element_type == 'float':
        converted_element = float(element)
    elif element_type == 'str':
        converted_element = str(element)
    elif element_type == 'bool':
        converted_element = bool(element)
    else:
        converted_element = element

    type_element = type(converted_element)

    var = (converted_element, type_element)
    data.append(var)
    i +=1

# printing data

print("So, data entered by you is in the form   =>  ['element you entered', 'type of that element']")
for i in data:
    print(i)
