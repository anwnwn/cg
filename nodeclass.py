class Node:
    def __init__(self, nodeID, nodeLabel):
        self.nodeid = nodeID
        self.nodelabel = nodeLabel
        self.parents = []
        self.children = []
        self.uniquereads = []
    
    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)

    
    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def add_readid(self, readID):
        if readID not in self.uniquereads:
            self.uniquereads.append(readID)

    def set_nodeid(self, nodeID):
        self.nodeid = nodeID