
# import os
# def parse_fasta_files(folder_path):
#     fasta_dict = {}
    
#     # Go thru all the files in the path
#     for filename in os.listdir(folder_path):
#         # Checks if it is a fasta file
#         if filename.endswith('.fasta') or filename.endswith('.fa'):
#             filepath = os.path.join(folder_path, filename)
#             try:
#                 with open(filepath, 'r') as file:
#                     sequence = ''
#                     for line in file:
#                         line = line.strip()
#                         if not line.startswith('>'):
#                             for c in line:
#                                 if c in ('ACGT'):
#                                     sequence += c
#                 # filename as key and sequence as value in dictionary
#                 fasta_dict[filename] = sequence
#             except Exception as e:
#                 print(f"Error reading {filename}: {e}")
#     return fasta_dict



# # # # ignore
# # # def build_suffix_tree(fasta_dict):
# # #     tree = {}
# # #     for key in fasta_dict:
# # #         sequence = fasta_dict[key]
# # #         for i in range(len(sequence)):
# # #             node = tree
# # #             for c in sequence[i:]:
# # #                 if c not in node:
# # #                     node[c] = {}
# # #                 node = node[c]
# # #     return tree

# # # def display(tree, level=0):    
# # #     for key in tree:
# # #         print(' ' * level + key)
# # #         display(tree[key], level + 1)



# # #actually i think this is a shitty trie not a shitty tree
# # class Node:
# #     def __init__(self):
# #         self.children = {}
# #         self.indexes = []

# # def build_suffix_tree(fasta_dict):
# #     root = Node()
# #     for seq_id, sequence in fasta_dict.items():
# #         for i in range(len(sequence)):
# #             current_node = root
# #             suffix = sequence[i:]
# #             for c in suffix:
# #                 if c not in current_node.children:
# #                     current_node.children[c] = Node()
# #                 current_node = current_node.children[c]
# #                 current_node.indexes.append((seq_id, i))
# #     return root

# # def display(node, level=0, max_level=5):
# #     if level > max_level:
# #         return
# #     for key, child in node.children.items():
# #         print(' ' * level + key + f" ({len(child.indexes)} sequences)")
# #         display(child, level + 1, max_level)





# #fr shitty tree
# class Node:
#     def __init__(self):
#         self.children = {}  # keys will be edge labels
#         self.indexes = []   # stores (seq_id, position)
#         self.is_leaf = False

# def build_suffix_tree(fasta_dict):
#     root = Node()
#     for seq_id, sequence in fasta_dict.items():
#         sequence += '$'
#         for i in range(len(sequence)):
#             current_node = root
#             suffix = sequence[i:]
#             j = 0
#             while j < len(suffix): 
#                 for edge_label, child_node in current_node.children.items():
#                     k = 0
#                     #longest common prefix
#                     while k < len(edge_label) and j + k < len(suffix) and edge_label[k] == suffix[j + k]:
#                         k += 1
#                     if k > 0:
#                         #split? or new suffix
#                         if k < len(edge_label):
#                             existing_child = child_node
#                             new_child = Node()
#                             new_child.children[edge_label[k:]] = existing_child
#                             new_child.indexes = existing_child.indexes.copy()
#                             child_node.children = new_child.children
#                             child_node.indexes = new_child.indexes
#                             child_node.is_leaf = False
                            

#                             del current_node.children[edge_label]
#                             current_node.children[edge_label[:k]] = child_node
#                             edge_label = edge_label[:k]

#                         current_node = child_node
#                         j += k
#                         break
#                 else: #new suffix
#                     new_child = Node()
#                     new_child.is_leaf = True
#                     new_child.indexes.append((seq_id, i))
#                     current_node.children[suffix[j:]] = new_child
#                     break
#             else: #matching suffix
#                 current_node.is_leaf = True
#                 current_node.indexes.append((seq_id, i))
#     return root

# def display(node, level=0, max_level=5):
#     if level > max_level:
#         if node.is_leaf:
#             print(' ' * level + '--leaf')
#         return
#     for edge_label, child in node.children.items():
#         print(' ' * level + edge_label + f" ({len(child.indexes)} sequences)")
#         display(child, level + len(edge_label), max_level)

# def find(node, substring):
#     current_node = node
#     idx = 0

#     while idx < len(substring):
#         found = False
#         for edge_label, child_node in current_node.children.items():
#             common_length = 0
#             min_length = min(len(edge_label), len(substring) - idx)
#             while (common_length < min_length and
#                    edge_label[common_length] == substring[idx + common_length]):
#                 common_length += 1
#             if common_length > 0:
#                 idx += common_length
#                 if   common_length == len(edge_label):
#                     current_node = child_node
#                     found = True
#                     break
#                 elif idx == len(substring):
#                     return True
#                 else:
#                     return False
#         if not found:
#             return False
#     return True






# # this one is better
# # pip install suffix-trees
# # pip install suffix_trees
#     # from suffix_trees import STree

# # def build_suffix_tree_op(fasta_dict):
# #     sequences = list(fasta_dict.values())
# #     concatenated_seq = '#'.join(sequences) + '$'
# #     tree = STree.STree(concatenated_seq)
# #     return tree










# folder_path = 'Data/small2'
# fasta_dict = parse_fasta_files(folder_path)
# # print(fasta_dict)
# for filename, sequence in fasta_dict.items():
#     print(f"{filename}: {sequence[:50]}...")
# tree = build_suffix_tree(fasta_dict)
# display(tree)
# print(find(tree, 'CTG'))



# # tree2 = build_suffix_tree_op(fasta_dict)
# # substring = 'CTG'
# # index = tree2.find(substring)
# # if index != -1:
# #     print(f"found at {index}")
# # else:
# #     print(f"not found")
# # # display(tree)




import os

def parse_fasta_files(folder_path):
    fasta_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.fasta') or filename.endswith('.fa'):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r') as file:
                    sequence = ''
                    for line in file:
                        line = line.strip()
                        if not line.startswith('>'):
                            for c in line:
                                if c in ('ACGT'):
                                    sequence += c
                fasta_dict[filename] = sequence
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return fasta_dict

class Node:
    def __init__(self):
        self.children = {}
        self.indexes = []
        self.is_leaf = False

def build_suffix_tree(fasta_dict):
    root = Node()
    for seq_id, sequence in fasta_dict.items():
        sequence += '$'  # Append unique terminator
        for i in range(len(sequence)):
            current_node = root
            suffix = sequence[i:]
            j = 0
            while j < len(suffix):
                found_edge = False
                # Copy the items to avoid modifying the dict during iteration
                children_items = list(current_node.children.items())
                for edge_label, child_node in children_items:
                    k = 0
                    # Find the longest common prefix between edge_label and suffix[j:]
                    while (k < len(edge_label) and j + k < len(suffix) and
                           edge_label[k] == suffix[j + k]):
                        k += 1
                    if k > 0:
                        # Edge splitting
                        if k < len(edge_label):
                            # Split the edge
                            existing_child = child_node
                            split_node = Node()
                            split_node.children[edge_label[k:]] = existing_child
                            split_node.is_leaf = False
                            split_node.indexes = existing_child.indexes.copy()

                            # Update current node's child
                            current_node.children[edge_label[:k]] = split_node
                            del current_node.children[edge_label]

                            # Prepare to add the remaining suffix
                            current_node = split_node
                            current_node.indexes.append((seq_id, i))
                            j += k
                        else:
                            # Move to the child node
                            current_node = child_node
                            current_node.indexes.append((seq_id, i))
                            j += k
                        found_edge = True
                        break
                if not found_edge:
                    # Add new edge and node
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

def count_variants(node, parent_seq_ids, all_seq_ids):
    node_seq_ids = set(seq_id for (seq_id, _) in node.indexes)
    count = 0
    if node_seq_ids != parent_seq_ids and node_seq_ids != all_seq_ids:
        count += 1
    for child in node.children.values():
        count += count_variants(child, node_seq_ids, all_seq_ids)
    return count

def main():
    folder_path = 'Data/DMPK'
    fasta_dict = parse_fasta_files(folder_path)
    tree = build_suffix_tree(fasta_dict)

    all_seq_ids = set(fasta_dict.keys())
    num_variants = count_variants(tree, all_seq_ids, all_seq_ids)
    print(f"Number of variants: {num_variants}")

if __name__ == "__main__":
    main()

