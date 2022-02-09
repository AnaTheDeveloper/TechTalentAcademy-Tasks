import numpy as np

# Numpy is a maths and scientific python library. Its valuable in the world of data science and is key for Machine Learning.
# NumPy stands for Numerical Python.
# NumPy is used for data analysis on arrays, it performs various tasks and handles large datasets effectively and efficiently at fast speeds.

# An array with one dimension is called a vector and two dimensions is called a matrix. array=np.array()

if __name__ == '__main__':

    #------------------BOOTCAMP NOTES------------------------#

    # One-dimensional array example
    one_dimensional_array = np.array([1, 2, 3])
    print("One dimensional array example: ", one_dimensional_array)

    print("-----------------------------------------------------------------------------------------------------")

    # Two-dimensional array example
    two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Two-dimensional array example: ", two_dimensional_array)

    print("-----------------------------------------------------------------------------------------------------")

    # Slicing Arrays example
    slicing_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("Slicing array example 1: ", slicing_array[1:5])
    print("Slicing array example 2: ", slicing_array[4:])
    print("Slicing array example 3: ", slicing_array[:4])
    print("Slicing array example 4: ", slicing_array[1:9:2])

    print("-----------------------------------------------------------------------------------------------------")

    # NP Zeros
    zeros = np.zeros(10) # or .ones()
    print("Zeros example: ", zeros)#

    two_dimensional_zeros = np.zeros((4,4))
    print("Two dimensional arrays using zeros: ", two_dimensional_zeros)

    print("-----------------------------------------------------------------------------------------------------")

    # Random Arrays
    random = np.random.rand(3,4) # 3 rows, 4 columns
    print("Random Array example: ", random)

    print("-----------------------------------------------------------------------------------------------------")

    # Eye
    eye = np.eye(6)
    print("Eyes example: ", eye) # Identity matrix

    print("-----------------------------------------------------------------------------------------------------")

    # Arange
    arange = np.arange(10)
    print("Arange example 1: ", arange)

    arange2 = np.arange(5, 15)
    print("Arange example 2: ", arange2)

    arange3 = np.arange(2, 15, 2)
    print("Arange example 3: ", arange3)
    # can pass decimals as increments - use nplinespace for decimal arrays though

    print("-----------------------------------------------------------------------------------------------------")

    # Reshaping
    reshaping_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # 1D to 2D
    newReshapedArray = reshaping_array.reshape(4, 3) # rows then columns when creating the matrix
    print("Reshaped array example 1d to 2d: ", newReshapedArray)

    reshaping_array2 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) # 1D array to 3D array
    newReshapedArray2 = reshaping_array2.reshape(2, 3, 2) # 2 matrices, 3 rows and 2 columns.
    print("Reshaped example 1d to 3d: ", newReshapedArray2)


    reshape = np.arange(1, 26).reshape(5, 5) #Take a range from 1 to 26 and then put it in a 5 row by 5 column table
    print("Arange and reshape example: ", reshape)
    # has to have value the same length as the matrix e.g. 1-26 would print 25 entities and the matrix would by 5 by 5 - 5*5 = 25!
    # Remember it does not count the stop 26!

    print("-----------------------------------------------------------------------------------------------------")

    # Arrays and math operations
    operational_array_example = np.arange(0, 5)
    print("Range from 0 to 5: ", operational_array_example)
    print("Range from 0 to 5 but -10 example: ", operational_array_example - 10)
    print("Take the range from 0 to 5 and Multiply example:", operational_array_example * 10)
    print("Take the range from 0 to 5 and Divide example:", operational_array_example / 10)
    print("Take the range from 0 to 5 and Power example:", operational_array_example ** 2)

    maths_a = np.arange(1, 10).reshape(3, 3)
    print("Take a range from 1 to 10 and put in in a 3 row by 3 column table: ", maths_a)

    print("-----------------------------------------------------------------------------------------------------")

    # Dot - Performs multi dimensional array calculations
    dot_a = np.arange(1, 10).reshape(3, 3)
    dot_b = np.arange(10, 19).reshape(3, 3)
    dot_c = np.dot(dot_a, dot_b)

    print("Dot example: ", dot_c)

    print("-----------------------------------------------------------------------------------------------------")

    # Sum
    sum_a = np.arange(1, 10).reshape(3, 3)
    sum_b = np.arange(10, 19).reshape(3, 3)
    sum_c = np.dot(sum_a, sum_b)
    print("Sum example: ", sum_c)

    total_sum = np.sum(sum_c)
    print("Adds the whole sum together: ", total_sum)

    # You can use np.sum on any matrix.
    print("This is sum_a: ", sum_a)
    sum1 = np.sum(sum_a)
    print("This is the total of sum_1 added together: ", sum1)

    # Sum by row and column
    # By column example
    sum_by_column_a = np.arange(1, 10).reshape(3, 3)
    sum_by_column_b = np.arange(10, 19).reshape(3, 3)
    sum_by_column_c = np.dot(sum_by_column_a, sum_by_column_b)

    print("Sum of column a and b added together to make c: ", sum_by_column_c)

    e = np.sum(sum_by_column_c, axis=0)

    print("Sum by column example: ", e)

    # By row example
    sum_by_row_a = np.arange(1, 10).reshape(3, 3)
    sum_by_row_b = np.arange(10, 19).reshape(3, 3)
    sum_by_row_c = np.dot(sum_by_row_a, sum_by_row_b)

    print("Sum of row a and b added together to make c: ", sum_by_row_c)

    ex = np.sum(sum_by_row_c, axis=1)

    print("Sum by row example: ", ex)