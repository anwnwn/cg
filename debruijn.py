from parse_fasta_folder import parse_fasta_files 
from nodeclass import Node

# Get Input Fasta Files for pangenome (PG)
fasta_dict = parse_fasta_files("./Data/DMPK")
# fasta_dict = parse_fasta_files("./Data/toy_dataset")



k = 31
k = k-1

kmer_set = set()
kmer_dic = {}
queue = []


fasta_names = list(fasta_dict.keys())

for i, key in enumerate(fasta_names):
    if i == 1:
        read = fasta_dict[key] + "$"
        readlen = len(read)
        node_idx = 0
        curr_node = ""
        prev_node = ""
        for j in range(0, readlen+1):
            node_kmer = read[j:j+k]
            if node_kmer not in kmer_set:
                kmer_set.add(node_kmer)
                new_node = Node(node_idx, node_kmer)
                kmer_dic[node_kmer] = new_node
                node_idx += 1

            curr_node = kmer_dic[node_kmer]
            # Link current node to prev_node
            if prev_node != "":
                curr_node.add_child(prev_node)
                prev_node.add_parent(curr_node)
            prev_node = curr_node

            print(curr_node.nodelabel)






# # Number the node in this function
# def bfs(visited, node):
#     visited.append(node)
#     queue.append(node)
#     nodeID_counter = 0
#     while queue:          # Creating loop to visit each node
#         m = queue.pop(0)
#         m.set_nodeid(nodeID_counter)
#         # print("-"*m.nodecolid, m.nodelabel, "(", m.nodeid, ")") 
#         nodeID_counter += 1
#         for child in m.children:
#             if child not in visited:
#                 visited.append(child)
#                 queue.append(child)

def bfs_write(visited, node, fw):
    visited.append(node)
    queue.append(node)
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        for m_child in m.children:
            fw.write("\tS" + str(m.nodeid) + " -> S" + str(m_child.nodeid) + " [ label = "+m_child.nodelabel+" ];\n")

        for child in m.children:
            if child not in visited:
                visited.append(child)
                queue.append(child)


outfile = "output.txt"

fw = open(outfile, "a")
fw.write("strict digraph  {\n")
# bfs(visited, kmer_dic["$"])
visited = []
bfs_write(visited, kmer_dic["$"], fw) #function for BFS
fw.write("}\n")
fw.close()