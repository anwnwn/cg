import os
import sys
from parse_fasta_folder import parse_fasta_files 
from Wheeler_Graph.debruijn import build_debruijn
from Wheeler_Graph.searchwheeler import search_wheeler
import subprocess   
import time
import tracemalloc  



def time_check_read(directory, read):
    start = time.time()
    found = search_wheeler(directory, read)
    end = time.time()
    elapsed_time = end - start
    return found, elapsed_time

def read_sequences_from_file(kmer_file):
    with open(kmer_file, 'r') as f:
        reads = [line.strip() for line in f.readlines()]
    return reads

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 wheeler.py <fasta_folder_path> <benchmarking_input_testing_file> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    kmer_file = sys.argv[2]
    output_file = sys.argv[3]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, os.path.basename(output_file))

    # k-mer size
    k_value = 31

    # Memory 
    tracemalloc.start()

    # Parse FASTA files and build k-mer index
    fasta_sequences = parse_fasta_files(folder_path)
    start_mem = tracemalloc.get_traced_memory()
    start_time = time.time()
    debruijn_filename = build_debruijn(fasta_sequences, k_value)
    # Run the shell script
    subprocess.run(["bash", "./Wheeler_Graph/create_wheeler_graph.sh", debruijn_filename])
    end_time = time.time()
    end_mem = tracemalloc.get_traced_memory()

    build_time = end_time - start_time

    out_name = debruijn_filename.split(".")[0]
    wheeler_directory = f"./Wheeler_Graph/out__{out_name}"

    reads = read_sequences_from_file(kmer_file)

    with open(output_file, 'w') as out_fh:
        out_fh.write(f"Time taken to build kmer index: {build_time:.10f} seconds\n")
        out_fh.write(f"Memory usage for building kmer index: {end_mem[0] - start_mem[0]} bytes (current), {end_mem[1]} bytes (peak)\n")

        for read in reads:
            found, query_time = time_check_read(wheeler_directory, read)
            out_fh.write(f"Read: {read}, Found: {found}, Time: {query_time:.10f} seconds\n")

    tracemalloc.stop()

if __name__ == "__main__":
    main()