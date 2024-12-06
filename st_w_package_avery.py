import os
import time
import tracemalloc  # For memory profiling
from suffix_trees.STree import STree  # Adjust import if needed

# Parse FASTA files
def parse_fasta_files(folder_path):
    fasta_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.fasta') or filename.endswith('.fa'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as file:
                sequence = ''
                for line in file:
                    line = line.strip()
                    if not line.startswith('>'):
                        sequence += ''.join(c for c in line)
                fasta_dict[filename] = sequence
    return fasta_dict

# Build suffix tree
def build_suffix_tree(fasta_dict):
    concatenated_sequence = '#'.join(fasta_dict.values()) + '$'
    tree = STree(concatenated_sequence)
    return tree, concatenated_sequence

# Read substrings from an input file
def read_substrings_from_file(input_file):
    with open(input_file, 'r') as file:
        substrings = [line.strip() for line in file.readlines()]
    return substrings

# Main function
def main():
    # Paths
    folder_path = 'DMPK'  # Replace with your folder path
    input_file = 'benchmarking_files/DMPK_input.txt'  # Replace with the path to your input file
    output_file = 'output.txt'  # File to save the results

    # Parse the FASTA files
    fasta_dict = parse_fasta_files(folder_path)
    print(f"Loaded {len(fasta_dict)} sequences from FASTA files.")

    # Profile memory and time for building the suffix tree
    tracemalloc.start()  # Start memory tracing
    start_time = time.time()  # Start timing
    tree, concatenated_sequence = build_suffix_tree(fasta_dict)
    end_time = time.time()  # End timing
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop memory tracing

    print(f"Suffix tree built in {end_time - start_time:.6f} seconds.")
    print(f"Memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB.")
    print(f"Concatenated sequence length: {len(concatenated_sequence)}")

    # Write build stats to the output file
    with open(output_file, 'w') as file:
        file.write(f"Suffix tree built in {end_time - start_time:.6f} seconds.\n")
        file.write(f"Memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB.\n")

    # Read substrings from the input file
    substrings = read_substrings_from_file(input_file)
    print(f"Loaded {len(substrings)} substrings from the input file.")

    # Search substrings and measure time
    results = []
    for substring in substrings:
        start_time = time.time()
        index = tree.find(substring)  # Adjust to tree.locate if find() fails
        end_time = time.time()
        found = index != -1
        search_time = end_time - start_time
        results.append((substring, found, search_time))
        print(f"Substring: '{substring}', Found: {found}, Time: {search_time:.10f} seconds")

    # Write substring search results to the output file
    with open(output_file, 'a') as file:  # Append to the same output file
        for substring, found, search_time in results:
            file.write(f"Substring: {substring}, Found: {found}, Time: {search_time:.10f} seconds\n")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
