import os
import sys
import collections
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files  # Assuming parse_fasta_files is in this module
import time
import tracemalloc  # Importing for memory profiling

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
    k_value = 31  # Value from paper, Used 3 for toy dataset, Used 31 for DMPK 
    output_file = sys.argv[2]
    kmer_file = sys.argv[3]

    # Start memory tracing
    tracemalloc.start()

    # Parse FASTA files and build k-mer index
    fasta_sequences = parse_fasta_files(folder_path)

    # Record memory usage for building the kmer index
    start_mem = tracemalloc.get_traced_memory()
    kmer_index = build_kmer_index(fasta_sequences, k_value)
    if 'GCTCCCTCTCCTAGGACCCTCCCCCCAAAA' in kmer_index.keys():
        print ('YASSSSSSS')
    end_mem = tracemalloc.get_traced_memory()

    print(f"Memory usage for building kmer index: {end_mem[0] - start_mem[0]} bytes (current), {end_mem[1]} bytes (peak)")

    kmers = read_kmers_from_file(kmer_file)

    with open(output_file, 'w') as out_fh:
        for kmer in kmers:
            found, query_time = time_find_kmer(kmer_index, kmer)
            out_fh.write(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.10f} seconds\n")
            print(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.10f} seconds")

    # Stop memory tracing
    tracemalloc.stop()

if __name__ == "__main__":
    main()
