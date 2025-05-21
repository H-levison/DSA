
# Define a class to represent a sparse matrix
class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Stores non-zero values as (row, col): value

    # Set a value at a specific position in the matrix
    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value

    # Get the value at a specific position; return 0 if not present
    def get_element(self, row, col):
        if (row, col) in self.data:
            return self.data[(row, col)]
        return 0
    
# Function to read a sparse matrix from a file
def read_sparse_matrix(file_path):
    with open(file_path, 'r') as f:
        # Read and validate the first two lines for rows and columns
        row_line = f.readline().strip()
        col_line = f.readline().strip()

        if not row_line.startswith("rows=") or not col_line.startswith("cols="):
            print("Invalid file format (missing rows= or cols=)")
            exit()

        # Extract number of rows and columns
        rows = int(row_line.split('=')[1])
        cols = int(col_line.split('=')[1])

        # Initialize an empty sparse matrix
        matrix = SparseMatrix(rows, cols)

        # Process the remaining lines for non-zero entries
        for line in f:
            line = line.strip().replace(" ", "")
            if not line:
                continue

            # Check if line is in proper tuple format (r, c, v)
            if line.startswith("(") and line.endswith(")"):
                parts = line[1:-1].split(',')

                # Check if all parts are valid integers
                if len(parts) == 3 and all(part.isdigit() or (part.startswith('-') and part[1:].isdigit()) for part in parts):
                    r, c, v = map(int, parts)
                    matrix.set_element(r, c, v)
                else:
                    print("Invalid data entry:", line)
                    exit()
            else:
                print("Invalid line format:", line)
                exit()

    return matrix
