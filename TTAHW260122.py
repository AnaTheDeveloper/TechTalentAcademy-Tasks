# Task 1
# Create your own Flow Diagram, a subject of your
# own choice, Example: Fast food order and convert it
# into code.

# ----------------------------------------------------------#

# -----------------SEE GIT READ ME FOR IMAGE----------------#

# ----------------------------------------------------------#

# #Task 2
# As an extension to the motorbike task that costs
# £2000 and loses 10% of its value every year. Set up
# a function that performs the calculation by passing
# in parameters. Then using a loop, print the value of
# the bike every following year until it falls below
# £1000.

import datetime

if __name__ == '__main__':

    def motorbike(value):

        current_year = datetime.datetime.now().year
        year_counter = 0

        if value < 1000:
            print("This motorbike is worthless!")
        else:
            while value > 1000:
                year_counter += 1
                current_year += 1
                print("Motorbike Value in " + str(current_year) + " is: ", value)
                value = value - 100
            print("It'll take " + str(year_counter) + " years for the value of the motorbike to fall until it reaches "
                                                      "£1000")


    motorbike(2000)

# #Task 3
# Write a program which will ask for two numbers
# from a user. Then offer an option menu to the user
# giving them a choice of Math’s operators. Once the
# user has selected which operator they wish to use,
# perform the calculation by using a procedure and
# passing parameters.

if __name__ == '__main__':

    # Users input not hardcoded and no parameters

    def calculator():

        users_first_number = int(input("Pick two random numbers. \n"
                                       "What is your first number? "))
        users_second_number = int(input("What is your second number? "))

        users_menu_option = int(input(" Choose your arithmatic operator! "
                                      "\n [1] Add "
                                      "\n [2] Subtract "
                                      "\n [3] Multiply "
                                      "\n [4] Divide "))

        try:
            if users_menu_option == 1:
                addition_answer = users_first_number + users_second_number
                print("The answer is: ", addition_answer)
            elif users_menu_option == 2:
                subtraction_answer = users_first_number - users_second_number
                print("The answer is: ", subtraction_answer)
            elif users_menu_option == 3:
                division_answer = users_first_number * users_second_number
                print("The answer is: ", division_answer)
            elif users_menu_option == 4:
                division_answer = users_first_number / users_second_number
                print("The answer is: ", division_answer)
            else:
                print("Please enter options 1 to 4!")
        except ZeroDivisionError:
            print("You can't divide by zero!")

    calculator()

    # Users numbers hardcoded and parameters

if __name__ == '__main__':

    def hardcoded_calculator(number1, number2):

        users_menu_option = int(input(" Choose your arithmatic operator! "
                                      "\n [1] Add "
                                      "\n [2] Subtract "
                                      "\n [3] Multiply "
                                      "\n [4] Divide "))
        try:
            if users_menu_option == 1:
                addition_answer = number1 + number2
                print("The answer is: ", addition_answer)
            elif users_menu_option == 2:
                subtraction_answer = number1 - number2
                print("The answer is: ", subtraction_answer)
            elif users_menu_option == 3:
                division_answer = number1 * number2
                print("The answer is: ", division_answer)
            elif users_menu_option == 4:
                division_answer = number1 / number2
                print("The answer is: ", division_answer)
            else:
                print("Please enter options 1 to 4!")
        except ZeroDivisionError:
            print("You can't divide by zero!")

    hardcoded_calculator(230, 25)

