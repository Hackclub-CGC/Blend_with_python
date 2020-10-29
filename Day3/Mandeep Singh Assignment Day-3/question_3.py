# Main Data

data = {}
run = True

while run:
    user_DOB = input("Enter your Date Of Birth: ")
    user_email = input("Enter your email: ")
    data[f"{user_email}"] = user_DOB

    # confirming user email and DOB

    print("*" * 100) # Decorator
    print(f"Your entered you date of Birth '{user_DOB}' and email '{user_email}'")
    confirm_data = input("To comfirm your Date of Birth and email enter 'yes' (otherwise 'no' to enter it again): ").lower()

    while confirm_data == "no":
        print("*" * 100) # Decorator
        del data[user_email]
        user_DOB_new = input("Enter your new Date Of Birth: ")
        user_email_new = input("Enter your new email: ")
        data[f"{user_email_new}"] = user_DOB_new

        print(f"Your entered you new Date of Birth '{user_DOB_new}' and new email '{user_email_new}'")
        confirm_data = input("To comfirm your Date of Birth and email enter 'yes' (otherwise 'no' to enter it again): ").lower()

    run_again = input("Do you want to store a new DATA of Date of Birth and email ('yes' or 'no'): ").lower()
    print("*" * 100) # Decorator
    if run_again == "no":
        run = False


print("=" * 100) # Decorator
print("So, data entered by you is in the form  =>      'email' : '(corresponding)date of birth'    ")
print(data) 
print("=" * 100) # Decorator
