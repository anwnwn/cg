How to run the our implementation of the suffix tree script on the DMPK dataset and output benchmarking results to st_output.txt within the directory:

Navigate to cg directory 

python3 -m Suffix_Tree.st_implementation.suffix_tree Data/DMPK Benchmarking_Files/output.txt st_output.txt

How to run the suffix tree package implementation of the suffix tree script on the DMPK dataset and output benchmarking results to st_output.txt within the directory:

Navigate to cg directory 

python3 -m Suffix_Tree.st_package_implementation.suffix_tree Data/DMPK Benchmarking_Files/output.txt st_output.txt

Generalized:
python3 -m <script file> <input data generated from benchmarking> <where you want benchmarking files outputted>

The format of the output file will be:
Line 1 - Time taken to build the suffix tree(seconds)
Line 2 -  Peak memory usage (in bytes)
Line 3+ - Length of read: query time(seconds)