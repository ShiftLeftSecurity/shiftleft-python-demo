"""
Assignment 2. Jeffrey Green. SDEV 300
"""


import ast
import datetime
import math
import secrets
import string
import sys

RUN_PROGRAM = True


def main():
    """
    Main function to present user menu.
    """
    print("Chose the letter of which program to run")
    print(" a. Generate Secure Password\n",
          "b. Calculate and Format a Percentage\n",
          "c. How many days from today until July 4, 2025?\n",
          "d. Use the Law of Cosines to calculate the leg of a triangle.\n",
          "e. Calculate the volume of a Right Circular Cylinder\n",
          "f. Exit program")
    return input("Which program to run?: ")


def valid_program(program):
    """
    Checks to see if valid program selected.
    """
    if program.lower() == "a":
        password()
    elif program.lower() == "b":
        percentage()
    elif program.lower() == "c":
        days_away()
    elif program.lower() == "d":
        law_of_cosine()
    elif program.lower() == "e":
        volume()
    elif program.lower() == "f":
        exit_program()
    else:
        print("Invalid selection. Select again.")


def password():
    """
    Generates secure password.
    """
    password_options = ""
    password_options_count = 0
    pass_correct = False
    upper_correct = False
    lower_correct = False
    num_correct = False
    symbol_correct = False

    def password_length():
        try:
            return ast.literal_eval(input("What will be the password length? "))
        except ValueError:
            print("Incorrect value. Try again.\n")

    def upper_char():
        return input("Use upper case characters? (Yes or No)")  # string.ascii_uppercase

    def lower_char():
        return input("Use lower case characters? (Yes or No)")  # string.ascii_lowercase

    def num_char():
        return input("Use numbers? (Yes or No)")  # string.digits

    def symbol_char():
        return input("Use symbols? (Yes or No)")  # string.punctuation

    while not pass_correct:
        pass_length = password_length()
        if isinstance(pass_length, int):
            if pass_length < 1:
                print("Number less than 1 entered.")
            else:
                pass_correct = True

    while not upper_correct:
        use_upper = upper_char().capitalize()
        if use_upper == "Yes":
            password_options += string.ascii_uppercase
            password_options_count += 26
            upper_correct = True
        elif use_upper == "No":
            upper_correct = True
        else:
            print("Incorrect entry. Please enter either Yes or No.\n")

    while not lower_correct:
        use_lower = lower_char().capitalize()
        if use_lower == "Yes":
            password_options += string.ascii_lowercase
            password_options_count += 26
            lower_correct = True
        elif use_lower == "No":
            lower_correct = True
        else:
            print("Incorrect entry. Please enter either Yes or No.\n")

    while not num_correct:
        use_num = num_char().capitalize()
        if use_num == "Yes":
            password_options += string.digits
            password_options_count += 10
            num_correct = True
        elif use_num == "No":
            num_correct = True
        else:
            print("Incorrect entry. Please enter either Yes or No.\n")

    while not symbol_correct:
        use_symbol = symbol_char().capitalize()
        if use_symbol == "Yes":
            password_options += string.punctuation
            password_options_count += 32
            symbol_correct = True
        elif use_symbol == "No":
            symbol_correct = True
        else:
            print("Incorrect entry. Please enter either Yes or No.\n")

    if use_upper.capitalize() == "No" and use_lower.capitalize() == "No" \
            and use_num.capitalize() == "No" and use_symbol.capitalize() == "No":
        print("Invalid selections. Returning to main menu.")
        return None

    user_password_str = ''.join(secrets.choice(password_options) for i in range(pass_length))

    print(f"Your system generated password is: {user_password_str}")


def percentage():
    """
    Function to find percentage.
    """
    numerator = ast.literal_eval(input("Enter the numerator. "))
    denominator = ast.literal_eval(input("Enter the denominator. "))
    decimal = ast.literal_eval(input("Enter the number of decimal points. "))

    percent = 100 * (numerator / denominator)

    print("Your percentage is: ", round(percent, decimal), "%.")


def days_away():
    """
    Function to find days between.
    """
    today = datetime.date.today()
    future = datetime.date(2025, 7, 4)
    print("It is currently", future - today, "days away from July 4, 2025.")


def law_of_cosine():
    """
    Function to find cosine.
    """
    side_a = 11
    side_b = 8
    angle_c = 37
    cosine = math.sqrt(side_a ** 2 + side_b ** 2 -
                       2 * side_a * side_b * math.cos(math.radians(angle_c)))

    print(
        f"Side a equals {side_a}, Side 2 equals {side_b}, "
        f"and the angle of the opposite side of c is {angle_c} degrees.")
    print(f"The length of side c equals {cosine}.")


def volume():
    """
    Function to find the volume of right cylinder.
    """
    radius = 6
    height = 6
    cyl_vol = (math.pi * radius ** 2) * height

    print(f"Radius equals {radius}, height equals {height}. The volume is {cyl_vol}.")


def exit_program():
    """
    Ends program
    """
    print("Thank you for using the program. Exiting now.")
    sys.exit()


while RUN_PROGRAM:
    valid_program(main())
    print()
