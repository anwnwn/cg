# Notebook Code Used: 
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_KmerIndexHash.ipynb
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/FASTQ.ipynb

import os
import sys
import collections
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files
import time
import tracemalloc  

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
        print("Usage: python3 kmer_index_implementation.py <fasta_folder_path> <output_file> <kmer_input_testing_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    # 3 for toy dataset, 31 for kmers
    k_value = 31  
    output_file = sys.argv[2]
    output_file = os.path.join(os.getcwd(), os.path.basename(output_file)) #ensuring that it is in the directory of kmer index
    kmer_file = sys.argv[3]

    # Memory tracing
    tracemalloc.start()

    # Parse FASTA files
    fasta_sequences = parse_fasta_files(folder_path)

    # Record memory usage and time for building the kmer index
    start_mem = tracemalloc.get_traced_memory()
    start_time = time.time()  # Start timing
    kmer_index = build_kmer_index(fasta_sequences, k_value)
    end_time = time.time()  # End timing
    end_mem = tracemalloc.get_traced_memory()

    build_time = end_time - start_time  # Time taken to build the index


    kmers = read_kmers_from_file(kmer_file)

    with open(output_file, 'w') as out_fh:
        out_fh.write(f"Time taken to build kmer index: {build_time:.10f} seconds\n")
        out_fh.write(f"Memory usage for building kmer index: {end_mem[0] - start_mem[0]} bytes (current), {end_mem[1]} bytes (peak)")
        out_fh.write(f"Time taken to build kmer index: {build_time:.10f} seconds")
        for kmer in kmers:
            found, query_time = time_find_kmer(kmer_index, kmer)
            out_fh.write(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.10f} seconds\n")
            print(f"K-mer: {kmer}, Found: {found}, Time: {query_time:.10f} seconds")

    # Stop memory tracing
    tracemalloc.stop()

if __name__ == "__main__":
    main()
