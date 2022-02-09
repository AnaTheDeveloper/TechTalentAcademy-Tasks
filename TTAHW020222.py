# Task 1
# Write a program that allows you to enter 4 numbers
# and stores them in a file called “Numbers” - 3, 45, 83, 21

def files():

    list_of_numbers = []

    n = int(input("How many numbers do you want to enter? : "))

    for i in range(0, n):
        print("Enter Number {}: ".format(i + 1))
        inputted_number = int(input())
        list_of_numbers.append(inputted_number)
    print("The list you entered is: ", list_of_numbers)

    my_file = open("numbers.txt", "w")

    for num in list_of_numbers:
        my_file.writelines(str(num)+'\n')

    my_file.close()

    # Simplified Version below
    # numlist =['123', '234', '345']
    # my_file = open("numbers.txt", "w")
    # for num in numlist:
    #     my_file.writelines(num+'\n')
    # my_file.close()

if __name__ == '__main__':
    files()

# Task 2
# Write a program to ask a student for their percentage mark and convert this to a grade.
# The conversion will be done in a function called mark_grade.

    def mark_grade(grade_percentage):

        grades_list = ["A*", "A", "B", "C", "D", "E", "F"]

        if grade_percentage >= 90:
            return grades_list[0]
        elif 80 <= grade_percentage < 90:
            return grades_list[1]
        elif 70 <= grade_percentage < 80:
            return grades_list[2]
        elif 60 <= grade_percentage < 70:
            return grades_list[3]
        elif 50 <= grade_percentage < 60:
            return grades_list[4]
        elif 40 <= grade_percentage < 80:
            return grades_list[5]
        else:
            return grades_list[6]

    users_percentage_mark = int(input("What percentage score did you get out of %100 on your exam?"))
    final_grade = mark_grade(users_percentage_mark)
    print("Your Grade is: " + final_grade)


# Extension to Task 2
# • Ask the user for their target grade and print this with their mark
# • If their target grade > exam grade display a suitable message
# • If their target grade = exam grade display a suitable message
# • If their target grade < exam grade display a suitable message

    users_target_grade = input("What is your target grade?")

    if users_target_grade == final_grade:
        print("You reached your target! Your grade: " + final_grade + " Target Grade: " + users_target_grade)
    elif users_target_grade == "A*" and final_grade == "A":
        print("Almost! Your grade: " + final_grade + " Target Grade: " + users_target_grade)
    elif users_target_grade == "A" and final_grade == "A*":
        print("You got higher than your target grade! Your grade: " + final_grade + " Target Grade: " + users_target_grade)
    elif users_target_grade < final_grade:
        print("You need to work harder Your grade: " + final_grade + " Target Grade: " + users_target_grade)
    else:
        print("Well done! Your grade: " + final_grade + " Target Grade: " + users_target_grade)
