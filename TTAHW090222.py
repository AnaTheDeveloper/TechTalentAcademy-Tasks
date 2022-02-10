import numpy as np

if __name__ == '__main__':
    # Task 1. Create a 1D array of numbers from 0 to 9

    oneD_array_from_0_to_9 = np.arange(10)
    print("One dimensional array from 0 to 9: ", oneD_array_from_0_to_9)

    # Task 2. Create a 3×3 NumPy array of all Boolean value Trues.

    threeByThree_array_of_booleans1 = np.array([[True, True, True], [True, True, True], [True, True, True]])
    print("Initial thinking of this task: ", threeByThree_array_of_booleans1)

    threeByThree_array_of_booleans2 = np.ones((3, 3), dtype=bool)
    print("The right way?: ", threeByThree_array_of_booleans2)

    # Task 3. Extract all odd numbers from array of 1-10.

    extract_odd_numbers = np.arange(11)
    print("Extracted odd numbers: ", extract_odd_numbers[extract_odd_numbers % 2 == 1])

    # Task 4. Replace all odd numbers in an array of 1-10 with the value -1.

    replaced_odd_numbers_with_minus_one = np.arange(1, 10, 1)

    replaced_odd_numbers_with_minus_one[replaced_odd_numbers_with_minus_one % 2 == 1] = -1

    print("Replaced odd numbers with -1: ", replaced_odd_numbers_with_minus_one)

    # Task 5. Convert a 1D array to a 2D array with 2 rows.

    oneDArray_too_twoDArray_with_two_rows = np.arange(20).reshape(2, 10)

    print("This is my reshaped array: ", oneDArray_too_twoDArray_with_two_rows)

    # Task 6. Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals.
    # Creating my two arrrays
    array_one = np.arange(1, 13)
    array_two = np.arange(13, 25)

    # This uses .vstack
    stacked_vertically = np.vstack((array_one, array_two))
    print("This is using vertical stack: ", stacked_vertically)
    vertical_stack_result = np.sum(stacked_vertically, axis=0)

    # Using .vstack and .dot
    dot = np.dot(array_one, array_two)
    x = np.sum(dot, axis=0)
    print("using dot: ", x)

    # This uses .column_stack
    column_stack = np.column_stack((array_one, array_two))
    print("This is using Colum stack: ", column_stack)
    colum_stack_result = np.sum(column_stack, axis=0)

    # Results of both ways printed out
    print("Vertical Stacks Results: ", vertical_stack_result)
    print("Column Stacks results: ", colum_stack_result)

    # Extension Task

# Task 1. Create the following pattern without hard coding. Use only NumPy functions. ie >array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3])

    # Organise array into pattern
    one_two_three_array = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])

    # Separate the first and second half.
    second_half_of_array = one_two_three_array[len(one_two_three_array) // 2:]
    print("The second half of the array is:, ", second_half_of_array)

    # Take first half and sort.
    matrix = np.matrix('[1,2,3]')
    newMatrix = matrix.repeat(3)
    print("First half: ", newMatrix)

    # Take second half
    matrix2 = np.matrix(second_half_of_array)
    newMatrix2 = matrix2.repeat(1)
    print("Second half: ", newMatrix2)

    # Take the two separate bits and put together
    task1 = np.concatenate((newMatrix, newMatrix2), axis=1)
    print("The answer to task 1: ", task1)

# Task 2. In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove all repeating items present in array b.

    array_a = np.array([1, 2, 3, 4, 5])
    array_b = np.array([4, 5, 6, 7, 8, 9])

    # Combine arrays and remove any repeating elements in array b.
    new_unique_array = array_a[array_b[np.searchsorted(array_b, array_a)] != array_a]
    print("The new unique array is: ", new_unique_array)

# Task 3. Get all items between 3 and 7 from a and b and sum them together.

    combined_array = np.concatenate((array_a, array_b))
    print("The combined array is: ", combined_array)
    sliced_array = combined_array[2:8]
    print("The sliced array is: ", sliced_array)
    new_sliced_array_sum = np.sum(sliced_array)
    print("The sliced array total is: ", new_sliced_array_sum)


# =========================TERMINAL OUTPUT============================#

# TASKS 1 TO 6

# One dimensional array from 0 to 9:  [0 1 2 3 4 5 6 7 8 9]

# Initial thinking of this task:  [[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

# The right way?:  [[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

# Extracted odd numbers:  [1 3 5 7 9]

# Replaced odd numbers with -1:  [-1  2 -1  4 -1  6 -1  8 -1]

# This is my reshaped array:  [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]]

# This is using vertical stack:  [[ 1  2  3  4  5  6  7  8  9 10 11 12]
#  [13 14 15 16 17 18 19 20 21 22 23 24]]

# using dot:  1586

# This is using Colum stack:  [[ 1 13]
#  [ 2 14]
#  [ 3 15]
#  [ 4 16]
#  [ 5 17]
#  [ 6 18]
#  [ 7 19]
#  [ 8 20]
#  [ 9 21]
#  [10 22]
#  [11 23]
#  [12 24]]

# Vertical Stacks Results:  [14 16 18 20 22 24 26 28 30 32 34 36]

# Column Stacks results:  [ 78 222]

#----------------------EXTENSION TASKS-------------------------#

# The second half of the array is:,  [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

# First half:  [[1 1 1 2 2 2 3 3 3]]

# Second half:  [[1 2 3 1 2 3 1 2 3]]

# The answer to task 1:  [[1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3]]

# The new unique array is:  [1 2 3]

# The combined array is:  [1 2 3 4 5 4 5 6 7 8 9]

# The sliced array is:  [3 4 5 4 5 6]

# The sliced array total is:  27

