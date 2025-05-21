from sparse_matrix import SparseMatrix

# Function to add two sparse matrices A and B
def add_matrices(A, B):
    # Check if both matrices have same dimensions
    if A.rows != B.rows or A.cols != B.cols:
       raise ValueError("Matrix sizes do not match for addition")

    # Create a result matrix with the same dimensions
    result = SparseMatrix(A.rows, A.cols)

    # Get all positions where either matrix has a non-zero value
    keys = set(A.data.keys()).union(B.data.keys())

     # Perform addition
    for (i, j) in keys:
        value = A.get_element(i, j) + B.get_element(i, j)
        result.set_element(i, j, value)

    return result

# Function to subtract matrix B from matrix A
def subtract_matrices(A, B):
    # Check if both matrices have same dimensions
    if A.rows != B.rows or A.cols != B.cols:
         raise ValueError("Matrix sizes do not match for subtraction")

    # Create a result matrix with the same dimensions
    result = SparseMatrix(A.rows, A.cols)

    # Get all positions where either matrix has a non-zero value
    keys = set(A.data.keys()).union(set(B.data.keys()))

    # Perform subtraction on corresponding elements
    for (i, j) in keys:
        value = A.get_element(i, j) - B.get_element(i, j)
        result.set_element(i, j, value)

    return result

# Function to multiply two sparse matrices A and B
def multiply_matrices(A, B):
    # Ensure the number of columns in A matches the number of rows in B
    if A.cols != B.rows:
         raise ValueError("Matrix sizes do not match for multiplication")

    # Create a result matrix with appropriate dimensions
    result = SparseMatrix(A.rows, B.cols)

     # Iterate through non-zero elements of A
    for (i, k), v1 in A.data.items():
        # Iterate through non-zero elements of B
        for (k2, j), v2 in B.data.items():
            # Check if the current elements of A and B are at the same position
            if k == k2:
                current = result.get_element(i, j)
                result.set_element(i, j, current + v1 * v2)
                
    return result