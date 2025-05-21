# Sparse Matrix Operations CLI Tool

## Overview

This project implements a command-line interface (CLI) tool to perform operations on large sparse matrices efficiently. The matrices are stored in text files and can be loaded, added, subtracted, or multiplied using this tool. It is designed to handle large input files with thousands of rows and columns by leveraging a sparse matrix representation, which optimizes storage and computation by only recording non-zero entries.

## Features

- **Load sparse matrices** from sample input files stored in a directory (`sample_inputs`).
- **Choose between three operations**:  
  1. Addition  
  2. Subtraction  
  3. Multiplication  
- **Select any two matrices** from available sample files by entering their corresponding numbers.
- **Efficient sparse matrix representation**: Only non-zero elements are stored internally to optimize performance and memory use.
- **Result output saved to a text file** called `results.txt` instead of printing long outputs to the terminal.
- User-friendly input prompts and error handling for invalid selections.

## Project Structure

```
/code
 ├── src
 │   ├── main.py            # Main CLI script to run operations
 │   ├── sparse_matrix.py   # Module containing sparse matrix reading and representation logic
 │   └── operations.py      # Module containing matrix operations: add, subtract, multiply
/sample_inputs
 ├── easy_sample_01_2.txt
 ├── easy_sample_01_3.txt
 ├── ...                   # Sample input matrix files in text format
results.txt                # Output file created after running the tool
```

## How It Works

1. **Sample Input Files**  
   The matrices are saved as text files under the `sample_inputs` directory. Each file represents a matrix with rows and columns; the format contains the matrix size and non-zero entries.

2. **Reading Sparse Matrices**  
   The tool reads these files using a function `read_sparse_matrix()` that builds an internal sparse matrix data structure, only keeping track of non-zero elements to minimize memory use.

3. **User Interaction**  
   - On running `main.py`, the user is prompted to select an operation: Add, Subtract, or Multiply.  
   - The program lists all available matrix files in `sample_inputs` with corresponding index numbers.  
   - The user selects two files by entering their numbers.  
   - The selected matrices are read and processed according to the chosen operation.

4. **Performing Operations**  
   Matrix addition, subtraction, and multiplication are performed using efficient algorithms that work with the sparse matrix format.

5. **Output**  
   The resulting matrix is saved to a file named `results.txt` in the same directory as the script. This prevents cluttering the terminal with large outputs and allows easier inspection and further processing.

## Usage

1. Make sure your current working directory is the project root, where `main.py` resides (e.g., `code/src`).

2. Ensure the `sample_inputs` folder is correctly placed relative to the script (`../sample_input` or adjusted in the code).

3. Run the program:
   ```bash
   python main.py
   ```

4. Follow the prompts:
   - Choose the operation (1, 2, or 3).
   - Select two matrix files by their displayed index numbers.

5. After completion, check `results.txt` for the output.

## Notes & Considerations

- **Handling Large Matrices**: The sparse matrix approach ensures that even very large matrices with thousands of rows and columns are processed efficiently, provided the data is mostly zeros.
- **File Paths**: The program uses relative paths to locate sample input files. If you move files or run the script from another directory, update the `folder` path in `list_sample_files()` accordingly.
- **Error Handling**: The current version assumes correct inputs from the user; invalid inputs will prompt a friendly error message.
- **Extensibility**: You can extend the program by adding more operations, matrix formats, or output options.

## Example

Sample interaction:

```
Choose an matrix operation:
1) Addition
2) Subtraction
3) Multiplication
Enter 1, 2 or 3: 2

The available matrix files in 'sample_inputs' are:
1) easy_sample_01_2.txt
2) easy_sample_01_3.txt

Enter the number for the first matrix file: 1
Enter the number for the second matrix file: 2

Reading matrix1.txt and matrix2.txt...
Result saved to results.txt
```

## Contact

If you have questions or want to contribute, feel free to reach out!
Linkedin- HonourGod Levison
Email- h.levison@alustudent.com