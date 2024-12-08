import os
import time
import tracemalloc
import sys
from parse_fasta_folder import parse_fasta_files 

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

    # Read substrings from input file
    with open(input_file, 'r') as file:
        substrings = [line.strip() for line in file.readlines()]

    # Search substrings, write results to output file
    with open(output_file, 'w') as out_fh:
        out_fh.write(f"{end_time - start_time:.6f}\n")
        out_fh.write(f"{end_mem[1]}\n")
        for substring in substrings:
            start_time = time.time()
            found = find(tree, substring)
            end_time = time.time()
            out_fh.write(f"{len(substring)}: {end_time - start_time:.10f}\n")

if __name__ == "__main__":
    main()