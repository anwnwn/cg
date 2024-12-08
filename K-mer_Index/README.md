How to run the kmer index script on the DMPK dataset and output benchmarking results to kmer_output.txt:

Navigate to the cg directory: 

For our case we ran:
python3 -m K-mer_Index.kmer_index_implementation Data/DMPK Benchmarking_Files/output.txt kmer_output.txt

Generalized:
python3 -m K-mer_Index.kmer_index_implementation <input data generated from benchmarking> <where you want benchmarking files outputted>
