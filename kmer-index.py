
# Notebook Code Used: 
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_KmerIndexHash.ipynb
# - https://nbviewer.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/FASTQ.ipynb


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
