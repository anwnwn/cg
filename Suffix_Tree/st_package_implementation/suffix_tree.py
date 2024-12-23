import os
import sys
import time
import tracemalloc  
from suffix_trees.STree import STree
from parse_fasta_folder import parse_fasta_files  

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
    if len(sys.argv) != 4:
        sys.exit(1)

    # Parse command-line arguments
    folder_path = sys.argv[1]
    input_file = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, os.path.basename(sys.argv[3]))

    # Parse the FASTA files
    fasta_dict = parse_fasta_files(folder_path)

    # Memory and time calculations
    tracemalloc.start()  # Start memory tracing
    start_time = time.time()  # Start timing
    tree, concatenated_sequence = build_suffix_tree(fasta_dict)
    end_time = time.time()  # End timing
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop memory tracing

    # Write stats to the output file
    with open(output_file, 'w') as file:
        file.write(f"{end_time - start_time:.6f}\n")
        file.write(f"{peak}\n")

    # Read substrings from the input file
    substrings = read_substrings_from_file(input_file)

    # Search substrings and measure time
    results = []
    for substring in substrings:
        start_time = time.time()
        index = tree.find(substring) 
        end_time = time.time()
        found = index != -1
        search_time = end_time - start_time
        results.append((substring, found, search_time))

    # Write substring search results to the output file
    with open(output_file, 'a') as file:  
        for substring in substrings:
            start_time = time.time()
            index = tree.find(substring) 
            end_time = time.time()
            search_time = end_time - start_time
            file.write(f"{len(substring)}: {search_time:.10f}\n")

if __name__ == "__main__":
    main()
