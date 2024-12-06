import os
import sys
import collections
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files  # Assuming parse_fasta_files is in this module
import time

# Builds a kmer index given fasta dict and a k value
def build_kmer_index(fasta_dict, k_value):
    kmer_index = defaultdict(list)
    for genome_id, sequence in fasta_dict.items():
        for i in range(len(sequence) - k_value + 1):
            kmer = sequence[i:i + k_value]
            kmer_index[kmer].append((i, genome_id))
    return kmer_index

# Reads kmers from a file
def read_kmers_from_file(kmer_file):
    with open(kmer_file, 'r') as f:
        kmers = [line.strip() for line in f.readlines()]
    return kmers

# Finding if a kmer exists and timing the operation
def time_find_kmer(kmer_index, kmer):
    start = time.time()
    found = kmer in kmer_index
    end = time.time()
    elapsed_time = end - start
    return found, elapsed_time

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kmer-index.py <fasta_folder_path> <output_file> <kmer_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    k_value = 31  # Value from paper
    output_file = sys.argv[2]
    kmer_file = sys.argv[3]

    fasta_sequences = parse_fasta_files(folder_path)
    kmer_index = build_kmer_index(fasta_sequences, k_value)
    kmers = read_kmers_from_file(kmer_file)

    with open(output_file, 'w') as out_fh:
        for kmer in kmers:
            found, query_time = time_find_kmer(kmer_index, kmer)
            out_fh.write(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.6f} seconds\n")
            print(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.6f} seconds")

if __name__ == "__main__":
    main()
