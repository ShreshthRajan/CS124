from strassen import *  
import matplotlib.pyplot as plt
import time

# Configuration for the range of matrix sizes to test
maxMatrixSizeExponent = 8

# Create a list of matrix sizes to test, from 2 to 2^maxMatrixSizeExponent
matrixSizes = [2**exp for exp in range(1, maxMatrixSizeExponent + 1)]

# Initialize lists to store runtime measurements
runtimesEfficientStrassen = [0] * maxMatrixSizeExponent
runtimesStandardMultiply = [0] * maxMatrixSizeExponent

for index, size in enumerate(matrixSizes):
    matrix_1 = create_binary_matrix(size)
    matrix_2 = create_binary_matrix(size)

    # Timing Strassen's algorithm
    start_time = time.time()
    strassen_result = efficient_strassen_multiplication(matrix_1, matrix_2)
    runtimesEfficientStrassen[index] = time.time() - start_time

    # Timing standard matrix multiplication
    start_time = time.time()
    standard_result = simple_matrix_multiply(matrix_1, matrix_2)
    runtimesStandardMultiply[index] = time.time() - start_time

# Visualization of runtime comparisons
plt.plot(matrixSizes, runtimesStandardMultiply, label="Standard Matrix Multiplication", color='blue')
plt.plot(matrixSizes, runtimesEfficientStrassen, label="Optimized Strassen's Algorithm", color='green')
plt.xlabel("Size of Matrix (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison: Standard vs. Optimized Strassen's")
plt.legend()
plt.grid(True)
plt.show()
