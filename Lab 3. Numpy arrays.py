import numpy as np
# Ex 1 . Create the following NumPy arrays:
# a) A 1-D array called zeros having 10 elements and all the elements are set to zero.
zeros = np.zeros(10, dtype=int)
print(f'\na)The array of zeros :{zeros}')

# b) A 1-D array called vowels having the elements ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’.
vowels = np.array(['a', 'e', 'i', 'o', 'u'])
print(f'\nb)The array by name vovewls :{vowels}')

# c) A 2-D array called ones having 2 rows and 5 columns and all the elements are set to 1 and dtype as int.
ones = np.ones((2, 5), dtype=int)
print(f'\nc)The array of ones :\n{ones}')

# d) Use nested Python lists to create a 2-D array called myarray1 having 3 rows and 3 columns and store the following data:
#  2.7, -2, -19
#  0, 3.4, 99.9
#  10.6, 0, 13
myarray1 = np.array([[2.7, -2, -19],
                     [0, 3.4, 99.9],
                     [10.6, 0, 13]])
print(f'\nd)The array by name myarray1:\n{myarray1}')

# e) A 2-D array called myarray2 using arange()
# having 3 rows and 5 columns with start value = 4, step size 4 and dtype as float.
myarray2 = np.arange(4, 4 + 3 * 5 * 4, 4, dtype=float).reshape(3, 5)
print(f'\ne)The array by name myarray2:\n{myarray2}', '\n')


# Ex 2. Using the arrays created in Exercise 1 above, write NumPy commands for the following:
# a) Find the dimensions, shape, size, data type of the items and itemsize of arrays zeros ,
# vowels , ones , myarray1 and myarray2.


def print_array_info(array_name, array):
    print(f"{array_name}:")
    print(f"  Dimensions: {array.ndim}")
    print(f"  Shape: {array.shape}")
    print(f"  Size: {array.size}")
    print(f"  Data type: {array.dtype}")
    print(f"  Item size: {array.itemsize} bytes")
    print()


print('\na)')
print_array_info('zeros', zeros)
print_array_info('vowels', vowels)
print_array_info('ones', ones)
print_array_info('myarray1', myarray1)
print_array_info('myarray2', myarray2)

# b) Reshape the array ones to have all the 10 elements in a single row.
ones_reshaped = ones.reshape(1, -1)
print("b) Reshaped 'ones' to a single row:\n", ones_reshaped)

# c) Display the 2nd and 3rd element of the array vowels.
second_element = vowels[1]
third_element = vowels[2]
print("\nc) The 2nd element of 'vowels':", second_element)
print("   The 3rd element of 'vowels':", third_element)

# d) Display all elements in the 2nd and 3rd row of the array myarray1.
rows_2_and_3 = myarray1[1:3]
print("\nd) Elements in the 2nd and 3rd row of 'myarray1':\n", rows_2_and_3)

# e) Display the elements in the 1st and 2nd column of the array myarray1.
columns_1_and_2 = myarray1[:, 0:2]
print("\ne) Elements in the 1st and 2nd column of 'myarray1':\n", columns_1_and_2)

# f) Display the elements in the 1st column of the 2nd and 3rd row of the array myarray1.
column_1_rows_2_and_3 = myarray1[1:3, 0]
print("\nf) Elements in the 1st column of the 2nd and 3rd row of 'myarray1':\n", column_1_rows_2_and_3)

# g) Reverse the array of vowels
vowels_reversed = vowels[::-1]
print("\ng) Reversed 'vowels':", vowels_reversed,'\n')


# Ex 1 Create the following NumPy arrays:
myarray1 = np.array([1, 2, 3, 4, 5])
myarray2 = np.array([6, 7, 8, 9, 10])

# a) Divide all elements of array ones by 3.
ones_divided = ones / 3
print("a) Array 'ones' divided by 3:\n", ones_divided)

# b) Add the arrays myarray1 and myarray2
sum_array = myarray1 + myarray2
print("\nb) Sum of myarray1 and myarray2:", sum_array)

# c) Subtract myarray1 from myarray2 and store the result in a new array.
diff_array = myarray2 - myarray1
print("\nc) Difference (myarray2 - myarray1):", diff_array)

# d) Multiply myarray1 and myarray2 elementwise.
product_array = myarray1 * myarray2
print("\nd) Elementwise multiplication of myarray1 and myarray2:", product_array)

# e) Do the matrix multiplication of myarray1 and myarray2 and store the result in a new array myarray3.
myarray3 = np.dot(myarray1, myarray2)
print("\ne) Matrix multiplication (myarray1 * myarray2):", myarray3)

# f) Divide myarray1 by myarray2.
division_array = myarray1 / myarray2
print("\nf) Elementwise division (myarray1 / myarray2):", division_array)

# g) Find the cube of all elements of myarray1 and divide the resulting array by 2.
cube_array = (myarray1 ** 3) / 2
print("\ng) Cube of myarray1 elements divided by 2:", cube_array)

# h)Find the square root of all elements of myarray2 and divide the resulting array by 2.
# The result should be rounded to two places of decimals.
sqrt_array = np.sqrt(myarray2) / 2
rounded_sqrt_array = np.round(sqrt_array, 2)
print("\nh) Square root of myarray2 divided by 2 (rounded to 2 places):", rounded_sqrt_array)


print()
# Ex 2. Create a 2-D array called myarray4 using arange() having 14 rows and 3 columns
# with start value = -1, step size 0.25 having. Split this array row wise into 3 equal
# parts and print the result.
myarray4 = np.arange(-1, -1 + 14 * 3 * 0.25, 0.25).reshape(14, 3)
split_arrays = np.array_split(myarray4, 3, axis=0)

print("2-D array 'myarray4':\n", myarray4)
print("\nSplit arrays:\n", split_arrays)

# Using the myarray4 created in the above questions, write commands for the following:
# a) Find the sum of all elements
sum_all_elements = np.sum(myarray4)
print("\na) Sum of all elements:", sum_all_elements)

# b) Find the sum of all elements row-wise
sum_row_wise = np.sum(myarray4, axis=1)
print("\nb) Sum of all elements row-wise:\n", sum_row_wise)

# c) Find the sum of all elements column-wise
sum_column_wise = np.sum(myarray4, axis=0)
print("\nc) Sum of all elements column-wise:\n", sum_column_wise)

# d) Find the max of all elements
max_all_elements = np.max(myarray4)
print("\nd) Max of all elements:", max_all_elements)

# e) Find the min of all elements in each row
min_per_row = np.min(myarray4, axis=1)
print("\ne) Min of all elements in each row:\n", min_per_row)

# f) Find the mean of all elements in each row
mean_per_row = np.mean(myarray4, axis=1)
print("\nf) Mean of all elements in each row:\n", mean_per_row)

# g) Find the standard deviation column-wise
std_column_wise = np.std(myarray4, axis=0)
print("\ng) Standard deviation column-wise:\n", std_column_wise)