How to run the kmer index script on the DMPK dataset and output benchmarking results to kmer_output.txt:

Navigate to the cg directory: 

For our case we ran:
python3 -m K-mer_Index.kmer_index_implementation Data/DMPK Benchmarking_Files/output.txt kmer_output.txt

Generalized:
python3 -m <script file> <input data generated from benchmarking> <where you want benchmarking files outputted>

The format of the output file will be:
Line 1 - Time taken to build the k-mer index(seconds)
Line 2 -  Peak memory usage (in bytes)
Line 3+ - Length of read: query time(seconds)




To construct and query wheeler graph, please follow the instructions below:

Generate DeBruijn Graph: python3 -m Wheeler_Graph.debruijn
Visualize DeBruijn Graph PNG (if Graphviz is downloaded): dot -Tpng [name of .dot file here] > [name of outputfile].png   
Create Wheeler Graph: 
Navigate to Wheelie Package Repository (Wheeler_Graph_Toolkit)
Move .dot file to ./bin (or adjust the command below)
% ./bin/recognizer  ./bin/[name of .dot file here] -w
Move the folder produced “out__[name of .dotfile]” to location of searchwheeler.py
Query Wheeler Graph: python3 searchwheeler.py
Change foldername to “out__[name of .dotfile]”
Change P 


