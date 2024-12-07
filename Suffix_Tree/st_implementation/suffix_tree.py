import os
import time
import tracemalloc
import sys
from parse_fasta_folder import parse_fasta_files 
import matplotlib.pyplot as plt
import pandas as pd

# Suffix Tree Node
class Node:
    def __init__(self):
        self.children = {}
        self.indexes = []
        self.is_leaf = False

# Build Suffix Tree
def build_suffix_tree(fasta_dict):
    root = Node()
    for seq_id, sequence in fasta_dict.items():
        sequence += '$'  # Append terminator
        for i in range(len(sequence)):
            current_node = root
            suffix = sequence[i:]
            j = 0
            while j < len(suffix):
                found_edge = False
                children_items = list(current_node.children.items())
                for edge_label, child_node in children_items:
                    k = 0
                    while (k < len(edge_label) and j + k < len(suffix) and
                           edge_label[k] == suffix[j + k]):
                        k += 1
                    if k > 0:
                        if k < len(edge_label):
                            existing_child = child_node
                            split_node = Node()
                            split_node.children[edge_label[k:]] = existing_child
                            split_node.is_leaf = False
                            split_node.indexes = existing_child.indexes.copy()

                            current_node.children[edge_label[:k]] = split_node
                            del current_node.children[edge_label]

                            current_node = split_node
                            current_node.indexes.append((seq_id, i))
                            j += k
                        else:
                            current_node = child_node
                            current_node.indexes.append((seq_id, i))
                            j += k
                        found_edge = True
                        break
                if not found_edge:
                    new_child = Node()
                    new_child.is_leaf = True
                    new_child.indexes.append((seq_id, i))
                    current_node.children[suffix[j:]] = new_child
                    current_node.indexes.append((seq_id, i))
                    break
            else:
                current_node.is_leaf = True
                current_node.indexes.append((seq_id, i))
    return root

# Search Substring
def find(node, substring):
    current_node = node
    idx = 0

    while idx < len(substring):
        found = False
        for edge_label, child_node in current_node.children.items():
            common_length = 0
            min_length = min(len(edge_label), len(substring) - idx)
            while (common_length < min_length and
                   edge_label[common_length] == substring[idx + common_length]):
                common_length += 1
            if common_length > 0:
                idx += common_length
                if common_length == len(edge_label):
                    current_node = child_node
                    found = True
                    break
                elif idx == len(substring):
                    return True
                else:
                    return False
        if not found:
            return False
    return True

# Main Function
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 suffix_tree.py <fasta_folder_path> <kmer_input_testing_file> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    input_file = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
    output_file = os.path.join(script_dir, os.path.basename(sys.argv[3]))  # Output file in script directory

    fasta_dict = parse_fasta_files(folder_path)

    # Memory and time for building the suffix tree
    tracemalloc.start()
    start_mem = tracemalloc.get_traced_memory()
    start_time = time.time()
    tree = build_suffix_tree(fasta_dict)
    end_time = time.time()
    end_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    strings = []
    lengths = [31, 62, 124, 248, 596]
    with open("Data/DMPK/dmpk_NM_001424164.fasta", "r") as file:
        # Skip the header line
        header = file.readline()
        
        # Read the remaining lines and concatenate them into a single sequence string
        sequence = "".join(line.strip() for line in file)

    # Extract substrings of specified lengths
    for i in lengths:
        if i <= len(sequence):  # Ensure the length is valid
            substring = sequence[:i]  # Get the substring of length i
            strings.append(substring)
        else:
            print(f"Length {i} exceeds the sequence length of {len(sequence)}.")

    # print(strings)


    substrings = strings



    # # Read substrings from input file
    # with open(input_file, 'r') as file:
    #     substrings = [line.strip() for line in file.readlines()]

    # Search substrings, write results to output file
    results = []
    with open(output_file, 'w') as out_fh:
        out_fh.write(f"Suffix tree built in {end_time - start_time:.6f} seconds\n")
        out_fh.write(f"Memory used: {end_mem[0] - start_mem[0]} bytes, Peak memory: {end_mem[1]} bytes\n")
        for substring in substrings:
            start_time = time.time()
            found = find(tree, substring)
            end_time = time.time()
            out_fh.write(f"Substring: {substring}, Found: {found}, Time: {end_time - start_time:.10f} seconds\n")
            print(f"Substring: {substring}, Found: {found}, Time: {end_time - start_time:.10f} seconds\n")
            results.append((substring, found, end_time - start_time))
            print( end_time - start_time)

    
    lengths = [len(substring) for substring, _, _ in results]
    times = [time for _, _, time in results]
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, times, marker='o', linestyle='-', label='Search Time')
    plt.xlabel('length of substring')
    plt.ylabel('query time')
    plt.grid(True)
    plt.legend()
    plt.show()
    print(results)



if __name__ == "__main__":
    main()
