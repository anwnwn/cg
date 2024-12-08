# This class was modified from DeBruijn Graph written by Ben Langmead, the link to the source code 
# https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_deBruijn.ipynb

# Modified lines are indicated below

import graphviz
from parse_fasta_folder import parse_fasta_files 


class DeBruijnGraph:
    ''' De Bruijn directed multigraph built from a collection of
        strings. User supplies strings and k-mer length k.  Nodes
        are k-1-mers.  An Edge corresponds to the k-mer that joins
        a left k-1-mer to a right k-1-mer. '''
 
    @staticmethod
    def chop(st, k):
        ''' Chop string into k-mers of given length '''
        for i in range(len(st)-(k-1)):
            yield (st[i:i+k], st[i:i+k-1], st[i+1:i+k])
    
    class Node:
        ''' Node representing a k-1 mer.  Keep track of # of
            incoming/outgoing edges so it's easy to check for
            balanced, semi-balanced. '''
        
        def __init__(self, km1mer):
            self.km1mer = km1mer
            self.nin = 0
            self.nout = 0
        
        def __hash__(self):
            return hash(self.km1mer)
        
        def __str__(self):
            return self.km1mer
    
    def __init__(self, strIter, k, circularize=False):
        ''' Build de Bruijn multigraph given string iterator and k-mer
            length k '''
        self.G = {}     # multimap from nodes to neighbors
        self.nodes = {} # maps k-1-mers to Node objects
        for st in strIter:
            if circularize:
                st += st[:k-1]
            for kmer, km1L, km1R in self.chop(st, k):
                nodeL, nodeR = None, None
                if km1L in self.nodes:
                    nodeL = self.nodes[km1L]
                else:
                    nodeL = self.nodes[km1L] = self.Node(km1L)
                if km1R in self.nodes:
                    nodeR = self.nodes[km1R]
                else:
                    nodeR = self.nodes[km1R] = self.Node(km1R)
                nodeL.nout += 1
                nodeR.nin += 1
                self.G.setdefault(nodeL, []).append(nodeR)
    
class DeBruijnGraph2(DeBruijnGraph):
    def to_dot(self):
        """ Return string with graphviz representation.  If 'weights'
            is true, label edges corresponding to distinct k-1-mers
            with weights, instead of drawing separate edges for
            k-1-mer copies. """
        g = graphviz.Digraph(comment='DeBruijn graph')
        for node in iter(self.G.keys()):
            g.node(node.km1mer, node.km1mer)
        for src, dsts in iter(self.G.items()):
            for dst in dsts:
                 # modification made to code: added label to edges
                g.edge(src.km1mer, dst.km1mer, label =str(dst.km1mer[-1])) 
        return g
    

def build_debruijn(fasta_dict, k_value): 

  

    # Concatenate pangenome reads, adding $ between each read
    fasta_names = list(fasta_dict.keys())
    read = ""
    for i, key in enumerate(fasta_names):
        read = read + fasta_dict[key] + "$"


    # Create Debruijn Graph in .Dot format
    dot = DeBruijnGraph2([read], k_value).to_dot()

    # Write .Dot file to output file
    dotname = "graphDMPKfinal.dot"
    outfile = "./Wheeler_Graph/" + dotname

    fw = open(outfile, "w")

    # Format to format accepted by Graphviz to render files and Wheelie Package
    lines_to_output = (dot.source).splitlines()
    for i,line in enumerate(lines_to_output): 
        if i == 0: 
            continue
        if i == 1 or i == len(lines_to_output) - 1: 
            fw.write(line + "\n")
        else: 
            fw.write(line + ";\n")
    fw.close()

    return dotname



if __name__ == "__main__":
    # Get Input Fasta Files for pangenome (PG)
    # fasta_dict = parse_fasta_files("./Data/toy_dataset")
    fasta_dict= parse_fasta_files("./Data/DMPK")
    build_debruijn(fasta_dict, 31)