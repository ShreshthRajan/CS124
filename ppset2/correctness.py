from output_styles import OutputStyles as outstyles
from strassen import *
import numpy as np

# Testing the accuracy of the modified matrix multiplication algorithms

# Test case 1: Validate results for 4x4 matrices, using powers of two
matrix_one_4 = create_binary_matrix(4)
matrix_two_4 = create_binary_matrix(4)

true_product_4 = np.matmul(matrix_one_4, matrix_two_4)
naive_product_4 = simple_matrix_multiply(matrix_one_4, matrix_two_4)
strassen_product_4 = efficient_strassen_multiplication(matrix_one_4, matrix_two_4)

if np.array_equal(true_product_4, naive_product_4):
    print(outstyles.PASS + "Test 1a: Standard Multiplication (4x4) Correct" + outstyles.RESET)
else:
    print(outstyles.FAIL + "Test 1a: Standard Multiplication (4x4) Incorrect" + outstyles.RESET)

if np.array_equal(true_product_4, strassen_product_4):
    print(outstyles.PASS + "Test 1b: Strassen Multiplication (4x4) Correct" + outstyles.RESET + "\n")
else:
    print(outstyles.FAIL + "Test 1b: Strassen Multiplication (4x4) Incorrect" + outstyles.RESET + "\n")


# Test case 2: Validate results for non-power-of-2 size, n = 9
matrix_one_9 = create_binary_matrix(9)
matrix_two_9 = create_binary_matrix(9)
true_product_9 = np.matmul(matrix_one_9, matrix_two_9)
naive_product_9 = simple_matrix_multiply(matrix_one_9, matrix_two_9)
strassen_product_9 = efficient_strassen_multiplication(matrix_one_9, matrix_two_9)

if np.array_equal(true_product_9, naive_product_9):
    print(outstyles.PASS + "Test 2a: Standard Multiplication (9x9) Correct" + outstyles.RESET)
else:
    print(outstyles.FAIL + "Test 2a: Standard Multiplication (9x9) Incorrect" + outstyles.RESET)

if np.array_equal(true_product_9, strassen_product_9):
    print(outstyles.PASS + "Test 2b: Strassen Multiplication (9x9) Correct" + outstyles.RESET + "\n")
else:
    print(outstyles.FAIL + "Test 2b: Strassen Multiplication (9x9) Incorrect" + outstyles.RESET + "\n")


# Test case 3: Validate results for non-power-of-2 and larger size, n = 150
matrix_one_150 = create_binary_matrix(150)
matrix_two_150 = create_binary_matrix(150)
true_product_150 = np.matmul(matrix_one_150, matrix_two_150)
naive_product_150 = simple_matrix_multiply(matrix_one_150, matrix_two_150)
strassen_product_150 = efficient_strassen_multiplication(matrix_one_150, matrix_two_150)

if np.array_equal(true_product_150, naive_product_150):
    print(outstyles.PASS + "Test 3a: Standard Multiplication (150x150) Correct" + outstyles.RESET)
else:
    print(outstyles.FAIL + "Test 3a: Standard Multiplication (150x150) Incorrect" + outstyles.RESET)

if np.array_equal(true_product_150, strassen_product_150):
    print(outstyles.PASS + "Test 3b: Strassen Multiplication (150x150) Correct" + outstyles.RESET + "\n")
else:
    print(outstyles.FAIL + "Test 3b: Strassen Multiplication (150x150) Incorrect" + outstyles.RESET + "\n")
