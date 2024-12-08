from parse_fasta_folder import parse_fasta_files 
from nodeclass import Node

# Get Input Fasta Files for pangenome (PG)
fasta_dict = parse_fasta_files("./Data/toypangenome")
# fasta_dict = parse_fasta_files("./Data/DMPK")
# fasta_dict = parse_fasta_files("./Data/toy_dataset")



k = 5
k = k-1

kmer_set = set()
kmer_dic = {}
queue = []


fasta_names = list(fasta_dict.keys())


for i, key in enumerate(fasta_names):
    read = fasta_dict[key] + "$"
    readlen = len(read)
    node_idx = 0
    curr_node = ""
    prev_node = ""
    for j in range(readlen + 1 -(k)):
        node_kmer = read[j:j+k]
        if node_kmer not in kmer_set:
            kmer_set.add(node_kmer)
            new_node = Node(node_idx, node_kmer)
            kmer_dic[node_kmer] = new_node
            node_idx += 1

        curr_node = kmer_dic[node_kmer]
        curr_node.add_readid(key)
        # Link current node to prev_node
        if prev_node != "":
            curr_node.add_child(prev_node)
            prev_node.add_parent(curr_node)
        prev_node = curr_node

        if "$" in node_kmer:
            print(curr_node.nodelabel)

        # print(curr_node.nodelabel)






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
            if "$" in m.nodelabel: 
                fw.write("\t" + str(m.nodelabel[:-1]) + " ->" + str(m_child.nodelabel) + " [ label = "+m.nodelabel[-2]+" ];\n")
            else:
                fw.write("\t" + str(m.nodelabel) + " ->" + str(m_child.nodelabel) + " [ label = "+m.nodelabel[-1]+" ];\n")

        for child in m.children:
            if child not in visited:
                visited.append(child)
                queue.append(child)


outfile = "output.dot"

fw = open(outfile, "w")
fw.write("strict digraph  {\n")
# bfs(visited, kmer_dic["$"])
visited = []
bfs_write(visited, kmer_dic["gat$"], fw) #function for BFS
fw.write("}\n")
fw.close()



# import graphviz
# g = graphviz.Digraph(comment='DeBruijn graph')
# for node in iter(kmer_dic.keys()):
#     g.node(kmer_dic[node].nodelabel,kmer_dic[node].nodelabel )
# visited = []
# queueu = []
# node = kmer_dic["GCGAATAAAAGGCCCTCCATCTGCCCAAA$"]
# visited.append(node)
# queue.append(node)
# while queue:          # Creating loop to visit each node
#     m = queue.pop(0)
#     for m_child in m.children:
#         g.edge(m.nodelabel, m_child.nodelabel)
#     for child in m.children:
#         if child not in visited:
#             visited.append(child)
#             queue.append(child)




