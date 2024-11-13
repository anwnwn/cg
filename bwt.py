from parse_fasta_folder import parse_fasta_files 

# Get Input Fasta Files for pangenome (PG)
# fasta_dict = parse_fasta_files("./Data/DMPK")
fasta_dict = parse_fasta_files("./Data/toy_dataset")


def concat_reads(fasta_dict): 
    long_read = ""
    for read in fasta_dict.values(): 
        long_read += (read + "$")
    return long_read
# Build BW Matrix 

def build_bw_matrix(fasta_dict):
    long_read = concat_reads(fasta_dict)
    rotations = set()
    read_double = long_read * 2
    rotations.update([read_double[i:i+len(long_read)] for i in range(len(long_read))])
    return (sorted(rotations))

def bwt_from_matrix(bwm):
    # Given bwm, returns bwt(t)
    return ''.join(map(lambda x: x[-1], bwm))


bw_matrix = build_bw_matrix(fasta_dict)

print(bwt_from_matrix(bw_matrix))
