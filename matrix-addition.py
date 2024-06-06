# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows = len(matrix1)
    cols = len(matrix1[0])

    # Create a new matrix to store the result
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform matrix addition
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

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
rows2 = int(input("\nEnter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = input_matrix(rows2, cols2)

# Check if the matrices have the same dimensions for addition
if rows1 != rows2 or cols1 != cols2:
    print("\nMatrix addition is not possible because the dimensions of the matrices are different.")
else:
    # Add the matrices
    result_matrix = add_matrices(matrix1, matrix2)

    # Print the result
    print("\nThe result of matrix addition is:")
    print_matrix(result_matrix)
