# Function to transpose a matrix
def transpose_matrix(matrix):
    # Get the dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    # Perform the transpose operation
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

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

# Get user input for the dimensions and elements of the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = input_matrix(rows, cols)

# Transpose the matrix
transpose = transpose_matrix(matrix)

# Print the original matrix
print("\nOriginal matrix:")
print_matrix(matrix)

# Print the transpose of the matrix
print("\nTranspose matrix:")
print_matrix(transpose)
