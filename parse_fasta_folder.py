# For usage purposes:
# from parse_fasta_folder import parse_fasta_files
# folder path = 'xyz'
# fasta_dict = parse_fasta_files(folder_path)

import os

def parse_fasta_files(folder_path):
    fasta_dict = {}
    
    # Go thru all the files in the path
    for filename in os.listdir(folder_path):
        # Checks if it is a fasta file
        if filename.endswith('.fasta') or filename.endswith('.fa'):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r') as file:
                    sequence = ''
                    for line in file:
                        line = line.strip()
                        if not line.startswith('>'):
                            for c in line:
                                # if c in ('ACGT'):
                                    sequence += c
                # filename as key and sequence as value in dictionary
                fasta_dict[filename] = sequence
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return fasta_dict

