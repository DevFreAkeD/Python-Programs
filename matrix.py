# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()  # for new line after each row

# Function to create a matrix from user input
def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Get user input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get user input for the matrix elements
matrix = input_matrix(rows, cols)

# Print the matrix
print("The matrix is:")
print_matrix(matrix)
