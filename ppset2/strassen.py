import numpy as np
import math
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# Generate a matrix with random binary entries
def create_binary_matrix(dim: int):
    return np.random.randint(0, 2, size=(dim, dim))

# Divide the matrix into quarters for processing
def quarter_matrix(matrix: np.ndarray):
    center = matrix.shape[0] // 2
    return matrix[:center, :center], matrix[:center, center:], matrix[center:, :center], matrix[center:, center:]

# Std matrix multiplication with a complexity of O(n^3)
def simple_matrix_multiply(mat1: np.ndarray, mat2: np.ndarray):
    dim = mat1.shape[0]
    output_matrix = np.zeros((dim, dim))

    for row in range(dim):
        for intermediary in range(dim):
            held_value = mat1[row, intermediary]
            for col in range(dim):
                output_matrix[row, col] += held_value * mat2[intermediary, col]
    return output_matrix

# Add padding to make matrix dimensions even for Strassen's method
def even_padding(matrix):
    num_rows, num_columns = matrix.shape
    pad_needed_rows = num_rows % 2 != 0
    pad_needed_cols = num_columns % 2 != 0
    if pad_needed_rows or pad_needed_cols:
        even_padding_config = ((0, int(pad_needed_rows)), (0, int(pad_needed_cols)))
        matrix = np.pad(matrix, even_padding_config, mode='constant', constant_values=0).astype(int)
    return matrix

# Strassen's matrix multiplication algorithm with a crossover threshold
def efficient_strassen_multiplication(mat1, mat2, base_threshold=105):
    dimension = mat1.shape[0]
    
    mat1 = even_padding(mat1)
    mat2 = even_padding(mat2)
    
    # Recursion termination condition
    if dimension <= base_threshold:
        computed_result = simple_matrix_multiply(mat1, mat2)
        return computed_result[:dimension, :dimension]
    
    mat1_11, mat1_12, mat1_21, mat1_22 = quarter_matrix(mat1)
    mat2_11, mat2_12, mat2_21, mat2_22 = quarter_matrix(mat2)
    
    # Compute the 7 intermediary products using concurrent processes
    with ThreadPoolExecutor() as pool:
        p1_future = pool.submit(efficient_strassen_multiplication, mat1_11, mat2_12 - mat2_22)
        p2_future = pool.submit(efficient_strassen_multiplication, mat1_11 + mat1_12, mat2_22)
        p3_future = pool.submit(efficient_strassen_multiplication, mat1_21 + mat1_22, mat2_11)
        p4_future = pool.submit(efficient_strassen_multiplication, mat1_22, mat2_21 - mat2_11)
        p5_future = pool.submit(efficient_strassen_multiplication, mat1_11 + mat1_22, mat2_11 + mat2_22)
        p6_future = pool.submit(efficient_strassen_multiplication, mat1_12 - mat1_22, mat2_21 + mat2_22)
        p7_future = pool.submit(efficient_strassen_multiplication, mat1_11 - mat1_21, mat2_11 + mat2_12)

        p1 = p1_future.result()
        p2 = p2_future.result()
        p3 = p3_future.result()
        p4 = p4_future.result()
        p5 = p5_future.result()
        p6 = p6_future.result()
        p7 = p7_future.result()

    
    top_left = p5 + p4 - p2 + p6
    top_right = p1 + p2
    bottom_left = p3 + p4
    bottom_right = p1 + p5 - p3 - p7

    composed_matrix_top = np.hstack((top_left, top_right))
    composed_matrix_bottom = np.hstack((bottom_left, bottom_right))
    composed_matrix = np.vstack((composed_matrix_top, composed_matrix_bottom))
    return composed_matrix[:dimension, :dimension].astype(int)

# Fetch and structure matrices from provided file path
def extract_matrices_from_file(file_path, size):
    with open(file_path, 'r') as file:
        raw_data = file.read().splitlines()
    raw_data = [int(val.strip()) for val in raw_data]
    mat_a = np.array(raw_data[:size**2]).reshape(size, size)
    mat_b = np.array(raw_data[size**2:]).reshape(size, size)
    return mat_a, mat_b

# Display diagonal elements of a matrix
def print_matrix_diagonal(matrix):
    for idx in range(matrix.shape[0]):
        print(int(matrix[idx, idx]))

# Main driver function
def run(flag, matrix_size, file_name):
    dim = int(matrix_size)
    matrix_one, matrix_two = extract_matrices_from_file(file_name, dim)
    final_product = efficient_strassen_multiplication(matrix_one, matrix_two)
    print_matrix_diagonal(final_product)

if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 4:
        print("Correct usage: python new_strassen.py <flag> <matrix_size> <file_name>")
    else:
        run(sys.argv[1], sys.argv[2], sys.argv[3])
