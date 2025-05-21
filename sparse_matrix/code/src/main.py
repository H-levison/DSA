import os
from sparse_matrix import read_sparse_matrix
from operations import add_matrices, subtract_matrices, multiply_matrices

# List all .txt files in the sample_inputs folder relative to this script
def list_sample_files():

    # Get the directory where the main.py script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to sample_inputs relative to script location
    folder = os.path.join(script_dir, "..", "..", "sample_inputs")
    folder = os.path.normpath(folder)

    # Filter only .txt files and sort them alphabetically
    files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])

    # Display the available sample files with index numbers
    for idx, f in enumerate(files, start=1):
        print(f"{idx}) {f}")
    return files

# Defining the main logic of the program
def main():
    # Prompt user to select a matrix operation
    print("Choose an matrix operation:")
    print("1) Addition\n2) Subtraction\n3) Multiplication")
    option = input("Enter 1, 2 or 3: ")

    # Show available matrix input files
    print("\nThe available matrix files in 'sample_input' are:")
    files = list_sample_files()

    # Get file selections from the user
    idx1 = int(input("\nEnter the number for the first matrix file you want to use: ")) - 1
    idx2 = int(input("Enter the number for the second matrix file you want to use: ")) - 1

    # Build full paths using the same base folder as list_sample_files()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_folder = os.path.normpath(os.path.join(script_dir, "..", "..", "sample_inputs"))
    file1 = os.path.join(base_folder, files[idx1])
    file2 = os.path.join(base_folder, files[idx2])

    # Load the matrices from the selected files
    print(f"\nReading {files[idx1]} and {files[idx2]}...")
    A = read_sparse_matrix(file1)
    B = read_sparse_matrix(file2)

    # Stop if loading failed
    if A is None or B is None:
        print("Failed to load matrices.")
        return

    # Perform the selected matrix operation
    if option == '1':
        result = add_matrices(A, B)
    elif option == '2':
        result = subtract_matrices(A, B)
    elif option == '3':
        result = multiply_matrices(A, B)
    else:
        print("You chose an invalid operation")
        return

    # If a result was returned, it writes a .txt file
    if result:
      output_file = "results.txt"
      with open(output_file, "w") as f:
        f.write("Resulting Matrix:\n")
        for key in sorted(result.data.keys()):
            f.write(f"({key[0]}, {key[1]}, {result.data[key]})\n")
        print(f"\nOperation result saved to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()