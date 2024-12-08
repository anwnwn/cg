import os
import sys

def extract_and_modify_substrings(input_file, output_file):

    # Can change the substring lengths you want to see as data
    substring_lengths = [31, 63, 127, 255, 511, 1024, 2047, 4095, 8191, 10000]
    start_index = 12  

    # Read the FASTA file
    try:
        with open(input_file, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Concatenate the sequence lines into one string ignoring the first line
    sequence = ''.join(line.strip() for line in content if not line.startswith('>'))

    # Check that sequence is long enough for the required substrings
    if len(sequence) < max(substring_lengths) + start_index:
        print(f"Error: The sequence length ({len(sequence)}) is shorter than the longest requested substring length ({max(substring_lengths)}) plus the start index ({start_index}).")
        sys.exit(1)

    # Extract substrings starting from the specified index
    substrings = []
    for length in substring_lengths:
        if len(sequence) >= length + start_index:
            original_substring = sequence[start_index:start_index + length]
            substrings.append(original_substring)

    # Write the substrings to the output file
    try:
        with open(output_file, 'w') as file:
            for substring in substrings:
                file.write(substring + '\n')
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 generate_test_data.py <fasta_file_path> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, os.path.basename(output_file))

    try:
        extract_and_modify_substrings(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()