import os
import sys
import random

def extract_random_substrings(input_file, output_file):
    """
    Extracts random substrings of specified lengths from a nucleotide sequence
    in a FASTA file and writes them to an output file.

    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output file.
    """
    substring_lengths = [31, 63, 127, 255, 511]

    # Read the FASTA file
    try:
        with open(input_file, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Concatenate the sequence lines into one string, ignoring the header
    sequence = ''.join(line.strip() for line in content if not line.startswith('>'))
    print(sequence)

    # Extract random substrings of specified lengths
    random_substrings = []
    for length in substring_lengths:
        if len(sequence) >= length:
            start_index = 0
            random_substrings.append(sequence[start_index:start_index + length])
        else:
            print(f"Warning: Sequence is too short to extract a substring of length {length}.")

    # Write the random substrings to the output file
    try:
        with open(output_file, 'w') as file:
            for substring in random_substrings:
                file.write(substring + '\n')
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_random_substrings.py <fasta_file_path> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the output file is created in the 'Benchmarking_Files' directory
    output_file = os.path.join(os.getcwd(), "Benchmarking_Files", os.path.basename(output_file))

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Ensure the output directory exists or create it
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Call the function to extract random substrings
    try:
        extract_random_substrings(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    print(f"Random substrings have been successfully written to '{output_file}'.")

if __name__ == "__main__":
    main()
