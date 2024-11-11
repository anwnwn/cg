
# Notebook Code Used: 
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_KmerIndexHash.ipynb
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/FASTQ.ipynb


<<<<<<< HEAD
import sys
import collections
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files

if len(sys.argv) != 4:
    print("Usage: python3 kmer-index.py <input_file> <k_value> <output_file>")
    sys.exit(1)

# Assign the input and output filenames from command-line arguments
fasta_file = sys.argv[1] # First argument: input filename
k_value = int(sys.argv[2]) # Second argument: output filename
output_file = sys.argv[3]


# Handle the fasta file and collect the valid bases in the file
with open(fasta_file, 'r') as fasta_file:
    fasta_input = ''
    for line in fasta_file:
        line = line.strip()
        if not line.startswith('>'):
            for c in line:
                if c in ('ACGT'):
                    fasta_input += c

# Read the value of k that is needed to build the k-mer index
with open(k_file, 'r') as k_file:
    k_index = k_file.readline().strip()
    k_index = int(k_index)

# Code modified from k-mer implementation from notebook 
index = collections.defaultdict()
for i in range(len(fasta_input) - k_index + 1):  # for each k-mer
    kmer = fasta_input[i:i+k_index]
    if kmer not in index:
        index[kmer] = [i]
    else:
        index[kmer].append(i)

#chatgpt

# import sys
# import collections
# from collections import defaultdict
# from Bio import SeqIO
# import os

# if len(sys.argv) != 4:
#     print("Usage: python3 hw2q2_pangenome.py <input_fasta_directory_or_file> <k_value> <output_file>")
#     sys.exit(1)

# # Assign the input and output filenames from command-line arguments
# input_path = sys.argv[1]  # Can be a directory or a multi-FASTA file
# k_index = int(sys.argv[2])  # k-mer size
# output_file = sys.argv[3]

# # Initialize the k-mer index
# kmer_index = defaultdict(set)

# # Function to process a single FASTA file
# def process_fastxa(file_handle, genome_id):
#     for record in SeqIO.parse(file_handle, "fasta"):
#         seq = str(record.seq).upper()
#         # Filter out non-ACGT characters
#         seq = ''.join([c for c in seq if c in ('A', 'C', 'G', 'T')])
#         for i in range(len(seq) - k_index + 1):
#             kmer = seq[i:i+k_index]
#             kmer_index[kmer].add(genome_id)

# # Check if input_path is a directory or a file
# if os.path.isdir(input_path):
#     # Iterate through all FASTA files in the directory
#     for filename in os.listdir(input_path):
#         if filename.endswith('.fasta') or filename.endswith('.fa') or filename.endswith('.fna'):
#             filepath = os.path.join(input_path, filename)
#             genome_id = os.path.splitext(filename)[0]  # Use filename (without extension) as genome ID
#             with open(filepath, 'r') as fh:
#                 print(f"Processing genome: {genome_id}")
#                 process_fasta(fh, genome_id)
# else:
#     # Assume it's a multi-FASTA file
#     with open(input_path, 'r') as fh:
#         for record in SeqIO.parse(fh, "fasta"):
#             genome_id = record.id  # Use FASTA header as genome ID
#             print(f"Processing genome: {genome_id}")
#             seq = str(record.seq).upper()
#             seq = ''.join([c for c in seq if c in ('A', 'C', 'G', 'T')])
#             for i in range(len(seq) - k_index + 1):
#                 kmer = seq[i:i+k_index]
#                 kmer_index[kmer].add(genome_id)

# # Write the k-mer index to the output file
# print(f"Writing k-mer index to {output_file}...")
# with open(output_file, 'w') as out_fh:
#     for kmer, genomes in kmer_index.items():
#         genomes_str = ','.join(genomes)
#         out_fh.write(f"{kmer}\t{genomes_str}\n")

# print("k-mer indexing for pangenome completed successfully.")
=======
import os
import sys
import collections
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files  # Assuming parse_fasta_files is in this module

# Builds a kmer index given fasta dict and a k value
def build_kmer_index(fasta_dict, k_value):
    kmer_index = defaultdict(list)
    # Iterate over the dictionary storing all the genome sequence info
    for genome_id, sequence in fasta_dict.items():
        for i in range(len(sequence) - k_value + 1):
            kmer = sequence[i:i + k_value]
            # key: kmer, value: index and genome id
            kmer_index[kmer].append((i, genome_id))

    return kmer_index

# Displaying the kmer index in output file
def write_kmer_index_to_file(kmer_index, output_file):
    with open(output_file, 'w') as out_fh:
        for kmer, positions in kmer_index.items():
            positions_str = ', '.join([f"{pos}@{genome_id}" for pos, genome_id in positions])
            out_fh.write(f"{kmer}\t{positions_str}\n")

# Finding if a kmer exists
def find_kmer(kmer_index, kmer):
    if kmer in kmer_index:
        return kmer_index[kmer]  
    else:
        return False 

# Locating all the variants and counting how many
def find_variants(kmer_index, genome_ids):

    variants = []
    total_genomes = set(genome_ids)

    for kmer, occurrences in kmer_index.items():
        seen = {genome_id for _, genome_id in occurrences}
        
        if seen != total_genomes:
            variants.append(kmer)

    return len(variants), variants


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kmer-index.py <fasta_folder_path> <k_value> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    k_value = int(sys.argv[2])
    output_file = sys.argv[3]

    fasta_sequences = parse_fasta_files(folder_path)

    kmer_index = build_kmer_index(fasta_sequences, k_value)

    write_kmer_index_to_file(kmer_index, output_file)

if __name__ == "__main__":
    main()
>>>>>>> 1411119 (can now take in DMPK folder, added functions that helps with displaying, finding kmer, and finding variants)
