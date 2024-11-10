
# Notebook Code Used: 
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_KmerIndexHash.ipynb
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/FASTQ.ipynb


import sys
import collections
from collections import defaultdict

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
