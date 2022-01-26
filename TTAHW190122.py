# Task 1
# Write a program that does the following:
# a) Stores a random number (1-10) in a variable – see hint below.
# b) Asks a user for their name and stores this in a variable.
# c) Asks a user to guess the number between 1 and 10.
# d) Tells the user whether they have guessed correctly.

import random

random_number = random.randint(1, 10)

user_stored_name = input("What is your name?")

print("Hi " + user_stored_name + " Im thinking of a random number between 0 and 10")

user_guess = int(input("What number am i thinking of? "))

if user_guess == random_number:
    print("You got it right!")
else:
    print("Try again! My number was " + str(random_number))

# #Task 2
# # Write a program that asks a user for their favourite number between 1
# # and 100 and then tells them a joke based on the number. You should
# # use a minimum of 3 jokes

random_number_between_1_and_100 = random.randint(1, 100)

users_number = int(input(user_stored_name + " Choose a number between 1 and 100 and i'll tell you a joke! "))

if users_number < 33:
    print("What is the most commonly used computer programming language? Profanity.")
elif users_number > 63 and users_number <= 84:
    print("What's a pirate's favourite programming language? R")
else:
    print("Roses are Red, Violets are Blue, Unexpected Indent, In line 22")

# Task 3
# Write a program that allows user to enter their favourite starter, main
# course, dessert and drink.
# Concatenate these and output a message which says – “Your favourite
# meal is ………with a glass of….”

users_fav_starter = str(input(user_stored_name + " Whats your favourite starter meal? "))
users_fav_maincourse = str(input(user_stored_name + " Whats your favourite main meal? "))
users_fav_desert = str(input(user_stored_name + " Whats your favourite desert? "))
users_fav_drink = str(input(user_stored_name + " Whats your favourite drink? "))

print(
    "So from what I understand. Your favourite starter is " + users_fav_starter + " with a main course of " + users_fav_maincourse +
    " and a glass of " + users_fav_drink + " and to finish it all off, some " + users_fav_desert)

# #Task 4
# # A motorbike costs £2000 and loses 10% of its value every year. Using a
# # loop, print the value of the bike every following year until it falls below
# # £1000

for x in range(2000, 900, -100):

    print("The motorbike is now: ", x)

    if x <= 1000:
        print("The motorbike has reached the lowest price possible.")

# Task 5
# Write a program which will ask for two numbers from a user. Then
# offer a menu to the user giving them a choice of operator:
# e.g. – Enter “a” if you want to add
# “b” if you want to subtract

print(user_stored_name + " Please pick two random numbers: ")
users_number_a = int(input(" What is your first random number? "))
users_number_b = int(input(" What is your second random number? "))

users_answear = int(input(" Choose your operator! Type '1' to add and '2' to suntract your numbers! "))

if users_answear == 1:
    random_numbers_answear = users_number_a + users_number_b
    print(random_numbers_answear)
elif users_answear == 2:
    random_numbers_answear2 = users_number_a - users_number_b
    print(random_numbers_answear2)
else:
    print("Please enter either 1 or 2")