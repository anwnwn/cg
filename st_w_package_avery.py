import os
import time
from suffix_trees import STree

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
                    sequence += ''.join(c for c in line if c in 'ACGT')
        fasta_dict[filename] = sequence
    return fasta_dict

def build_suffix_tree(fasta_dict):
    concatenated_sequence = '#'.join(fasta_dict.values()) + '$'
    tree = STree.STree(concatenated_sequence)
    return tree, concatenated_sequence

def main():
    # Folder containing FASTA files
    folder_path = 'Data/DMPK'  # Replace with your folder path
    substring = 'ZZ'
    # Parse the FASTA files
    fasta_dict = parse_fasta_files(folder_path)
    print(f"Loaded {len(fasta_dict)} sequences from FASTA files.")

    # Build the suffix tree
    tree, concatenated_sequence = build_suffix_tree(fasta_dict)

    # Search for the substring and measure search time
    start_time = time.time()
    index = tree.find(substring)
    end_time = time.time()

    # Output the results
    if index != -1:
        print(f"The substring '{substring}' exists in the pangenome at index {index}.")
    else:
        print(f"The substring '{substring}' does not exist in the pangenome.")
    print(f"Search time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
