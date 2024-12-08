
class WheelerGraphIndex:
    def __init__(self, L, I, O):
        self.L = L
        self.I = I
        self.O = O
        self.F = "".join(sorted(L)) 
        
        
        # Build C array (like first in FM-index)
        # C stores indices where a new character starts and ends in F
        indices = [0]
        # Get start indices of each new character of F
        for i in range(1, len(self.F)):
            string = self.F
            if string[i] != string[i - 1]:
                indices.append(i)
        self.C = dict(zip(sorted(set(L)),indices))

        # Add the index where each character ends
        for i, key in enumerate(self.C.keys()):
            if i == len(self.C) -1:
                self.C[key] = [self.C[key]]
                self.C[key].append(len(L) -1)
            else:
                self.C[key] = [self.C[key]]
                self.C[key].append(indices[i + 1] -1)
            
                
        # Helper Function to get indices for 1s and 0s of I and O
        def zeros_ones_helper(string): 
            zeros = []
            ones = []
            for i in range(len(string)):
                if string[i] == "0":
                    zeros.append(i)
                else: 
                    ones.append(i)
            return zeros, ones
            
        self.I_zeros, self.I_ones = zeros_ones_helper(self.I)
        self.O_zeros, self.O_ones = zeros_ones_helper(self.O)
        
        
    def i_select_0(self, low, high):
        # Get positions of 0's corresponding to the characters in F
        # 0's represent incoming edges
        return self.I_zeros[low], self.I_zeros[high]
        
    def i_rank_1(self, low, high):
        # Get ranks of the 1's corresponding to the nodes 
        low_1, high_1 = -1, -1
        for i in range(len(self.I_ones)):
            if self.I_ones[i] < low:
                continue
            elif self.I_ones[i] > low and low_1 == -1:
                low_1 = i
            elif self.I_ones[i] > high and self.I_ones[i] == high + 1:
                high_1 = i
                break      
        if low == high: 
            return low_1, low_1
        
        return low_1, high_1
        
    def o_select_1(self, low, high): 
        # Get positions of 1's corresponding to the nodes
        if low == -1: 
            return 0, self.O_ones[high]
        if high == -1: 
            return self.O_ones[low], len(self.O) - 1
        
        if high - low == 1: 
            return self.O_ones[low], self.O_ones[low]
        
        return self.O_ones[low], self.O_ones[high]
    
    def o_rank_0(self, low, high):
        # Get ranks of the 0's corresponding to the outgoing edges
        low_0, high_0 = -1, -1
        for i in range(len(self.O_zeros)):
            if self.O_zeros[i] < low:
                continue
            elif self.O_zeros[i] == low + 1:
                low_0 = i
            elif self.O_zeros[i] == high - 1:
                high_0 = i
                break
                
        if low == high: 
            return low_0, low_0
        return low_0, high_0
    
    def l_rank_c(self, low, high, char): 
        # Get ranks of the characters next in the search sequences
        indices = []
        counter = 0 
        for i in range(high + 1):
            if self.L[i] == char:
                if i >= low:
                    indices.append(counter)
                counter += 1
                
        return indices
                
    
    def backward_search(self,P):
        # This function performs the series of Rank, Select Queries to Search of Patterns in Wheeler Graph 
        indices = []
        for i in range(len(P) - 1, -1, -1): # Iterate through the pattern backwards
            c = P[i]

            if i == len(P) -1:  # At the first iteration, search the full range of the character
                start, stop = self.C[c][0], self.C[c][1]

            # At next iterations, get the range of characters to search based on l_rank
            elif len(indices) == 1: 
                start, stop = self.C[c][0] + indices[0], self.C[c][0] + indices[0]
            elif len(indices) > 1:
                start, stop = self.C[c][0] + indices[0], self.C[c][0] + indices[-1]
                
            # For Debugging: print("\n C[c]: " + str(start) + ", " + str(stop))

            I_low, I_high = self.i_select_0(start,stop)
            # For Debugging: print("i_select_0: " + str(I_low) + ", " + str(I_high))
            I_start, I_stop = self.i_rank_1(I_low,I_high)
            # For Debugging: print("i_rank_1: " + str(I_start) + ", " + str( I_stop))

            if I_start > 0:
                O_low,O_high = self.o_select_1(I_start -1, I_stop)
            else: 
                O_low,O_high = self.o_select_1(-1, I_stop)
            # For Debugging: print("o_select_1: " + str(O_low) + ", " +  str(O_high))
            O_start, O_stop = self.o_rank_0(O_low, O_high)
            # For Debugging: print("o_rank_0: " + str(O_start) + ", " + str(O_stop))

            if i > 0:
                if O_stop == -1:
                    O_stop = O_start
                # For Debugging: print(P[i:len(P) - 1] + " found")
                indices = self.l_rank_c(O_start, O_stop, P[i-1])
                # For Debugging: print(f"{P[i-1]} indices: {indices}")
                
                # If the next character is not found in L in the range, the pattern is not found
                if len(indices) == 0: 
                    return False
                # If the character found is the first character of P, the entire patter is found
                if i == 1 and len(indices)> 0: 
                    return True
                
                                                
        return False
        


            
# Ouput of Wheelie Package Creates a directory with the following files:
# L.txt (contains edge labels in order)
# I.txt (bitvector for incoming edges, probably as a string of '0' and '1')
# O.txt (bitvector for outgoing edges)
# nodes.txt (mapping node ordering to original node label)
# graph.dot (file to visualize wheeler order and edge labels - 1 based indexing)

def load_L(filename):
    # Assume L is stored as a single line of characters
    with open(filename, 'r') as f:
        L_str = f.read().strip()  # one string of characters
    return L_str

def load_bitvector(filename):
    # Assume I and O are stored as a string of '0'/'1' characters in a single line
    with open(filename, 'r') as f:
        bit_str = f.read().strip()
    return bit_str


foldername = "out__DMPK"

L_file = f"./{foldername}/L.txt"       # contains the edge labels in order
I_file = f"./{foldername}/I.txt"       # bitvector of incoming edges
O_file = f"./{foldername}/O.txt"       # bitvector of outgoing edges

# Load data
L_str = load_L(L_file)
I_str = load_bitvector(I_file)
O_str = load_bitvector(O_file)

# P = "GCTCCCTCTCCTAGGACCCTCCCCCCAAAAG" # Should return True
P = "CCTAGGACCCCCACCCCCGACCCTCGCGAAA" # Should return False
search_input = P[::-1] # reverse search string

wgi = WheelerGraphIndex(L_str, I_str, O_str)

found = wgi.backward_search(search_input)


if found:
        print(f"TRUE: '{P}' found in Wheeler Graph.")
else:
    print(f"FALSE: No occurences of '{P}' were found in Wheeler Graph")

