# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])

    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()  # for new line after each row

# Function to input a matrix from user
def input_matrix(rows, cols):
    matrix = []
    print("\nEnter the elements row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Get user input for the dimensions and elements of the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = input_matrix(rows1, cols1)

# Get user input for the dimensions and elements of the second matrix
# Note: The number of rows of the second matrix must be equal to the number of columns of the first matrix
rows2 = cols1
cols2 = int(input("\nEnter the number of columns for the second matrix: "))
matrix2 = input_matrix(rows2, cols2)

# Check if the matrices can be multiplied
if cols1 != rows2:
    print("\nMatrix multiplication is not possible with the given dimensions.")
else:
    # Multiply the matrices
    result_matrix = multiply_matrices(matrix1, matrix2)

    # Print the resulting matrix
    print("]nThe result of matrix multiplication is:")
    print_matrix(result_matrix)
