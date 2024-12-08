import os
import sys
from collections import defaultdict
from parse_fasta_folder import parse_fasta_files
import time
import tracemalloc  

def build_kmer_index(fasta_dict, k_value):
    kmer_index = defaultdict(list)
    for genome_id, sequence in fasta_dict.items():
        for i in range(len(sequence) - k_value + 1):
            kmer = sequence[i:i + k_value]
            kmer_index[kmer].append((i, genome_id))
    return kmer_index

def read_sequences_from_file(kmer_file):
    with open(kmer_file, 'r') as f:
        reads = [line.strip() for line in f.readlines()]
    return reads

def check_read_in_pangenome(kmer_index, read, k_value):
    # If the read is shorter than k_value not possible to produce a k-mer of length k_value.
    if len(read) < k_value:
        return False

    # Find all k-mers of length k_value from the read
    for i in range(len(read) - k_value + 1):
        kmer = read[i:i + k_value]
        # If any 31-mer from the read is not in the pangenome dictionary it is False
        if kmer not in kmer_index:
            return False

    # All 31-mers were found in the dictionary
    return True

def time_check_read(kmer_index, read, k_value):
    start = time.time()
    found = check_read_in_pangenome(kmer_index, read, k_value)
    end = time.time()
    elapsed_time = end - start
    return found, elapsed_time

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kmer_index_implementation.py <fasta_folder_path> <kmer_input_testing_file> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    kmer_file = sys.argv[2]
    output_file = sys.argv[3]

    # k-mer size
    k_value = 31

    # Memory 
    tracemalloc.start()

    # Parse FASTA files and build k-mer index
    fasta_sequences = parse_fasta_files(folder_path)
    start_mem = tracemalloc.get_traced_memory()
    start_time = time.time()
    kmer_index = build_kmer_index(fasta_sequences, k_value)
    end_time = time.time()
    end_mem = tracemalloc.get_traced_memory()

    build_time = end_time - start_time

    reads = read_sequences_from_file(kmer_file)

    with open(output_file, 'w') as out_fh:
        out_fh.write(f"Time taken to build kmer index: {build_time:.10f} seconds\n")
        out_fh.write(f"Memory usage for building kmer index: {end_mem[0] - start_mem[0]} bytes (current), {end_mem[1]} bytes (peak)\n")

        for read in reads:
            found, query_time = time_check_read(kmer_index, read, k_value)
            out_fh.write(f"Read: {read}, Found: {found}, Time: {query_time:.10f} seconds\n")
            print(f"Read: {read}, Found: {found}, Time: {query_time:.10f} seconds")

    tracemalloc.stop()

if __name__ == "__main__":
    main()