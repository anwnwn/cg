
# Pangenome Query Optimization using Wheeler Graphs
Repository for Computational Genomics Fall 2024, Group 4d

## Writeup 
Located in the Documents directory 

## Abstract
Reference bias, the tendency for genetic analyses to favor sequences similar to a single linear reference genome, often leads to the misalignment or exclusion of reads, resulting in incomplete variant detection and biased genomic studies. Pangenomes address these limitations by capturing the full spectrum of genetic diversity within a species, incorporating core, accessory, and variant sequences to enable more comprehensive and equitable analyses. However, existing approaches for pangenome analysis, such as multiple sequence alignment, k-mer indexes, suffix trees, de Bruijn graphs, and variation graphs, exhibit distinct trade-offs in scalability, storage efficiency, and query performance. To facilitate greater adoption of pangenomes over traditional linear reference genomes, there is a critical need for novel data structures that can efficiently store and query the vast diversity of genetic information while maintaining computational feasibility at scale. This paper explores the application of Wheeler Graphs to pangenome storage and querying, leveraging their path coherence and compression properties. Wheeler Graphs allow for efficient pattern matching and storage by encoding repetitive sequences and their variations in a succinct, ordered structure. Using a dataset that includes 14 variants of the DMPK gene, a gene with clinically significant repeat expansions, we benchmark the Wheeler Graph implementation against custom implementations of k-mer indexes and suffix trees. Results demonstrate that Wheeler Graphs achieve superior storage efficiency and competitive query performance while significantly reducing memory usage. These findings position Wheeler Graphs as a promising framework for scalable pangenome analysis, paving the way for more inclusive and accurate genomic studies.


## How to run
Each indexing representation (K-mer_Index, Suffix_Tree, Wheeler_Graph) can be accessed through its respective folder. All scripts can be run starting from the /cg directory.

#### K-mer index
- DMPK, write results to kmer_output.txt:
```
python3 -m K-mer_Index.kmer_index_implementation Data/DMPK Benchmarking_Files/output.txt kmer_output.txt
```
- generalized
```
python3 -m <script file>
```
The format of the output file will be:
```
Line 1 - Time taken to build the k-mer index(seconds)

Line 2 - Peak memory usage (in bytes)

Line 3+ - Length of read: query time(seconds)
```

#### Suffix tree
To run the proprietary implementation
- DMPK, write results to st_output.txt
```
python3 -m Suffix_Tree.st_implementation.suffix_tree Data/DMPK Benchmarking_Files/output.txt st_output.txt
```
To run the suffix tree package implementation
- DMPK, write results to st_output.txt
```
python3 -m Suffix_Tree.st_package_implementation.suffix_tree Data/DMPK Benchmarking_Files/output.txt st_output.txt
```
Generalized
```
python3 -m <script file>
```
The format of the output file will be: 
```
Line 1 - Time taken to build the suffix tree(seconds)
Line 2 - Peak memory usage (in bytes)
Line 3+ - Length of read: query time(seconds)
```

#### Wheeler graph

The Wheeler graph representation is generated through the Debruijn implementation and then fed through the Wheelie algorithm.

To generate DeBruijn graph
```
python3 -m Wheeler_Graph.debruijn Visualize DeBruijn Graph PNG (if Graphviz is downloaded): dot -Tpng [name of .dot file here] > [name of outputfile].png
```

To create Wheeler Graph
- Navigate to Wheelie Package Repository (Wheeler_Graph_Toolkit)
- Move .dot file to ./bin (or adjust the command below)
  ```
  % ./bin/recognizer ./bin/[name of .dot file here] -w
  ```
- Move the folder produced “out__[name of .dotfile]” to location of searchwheeler.py

To query Wheeler Graph
```
python3 searchwheeler.py Change foldername to “out__[name of .dotfile]” Change P
```

#### Reproducibility
To generate benchmarking data

- DMPK, write results to output.txt
  ```
  python3 generate_test_data.py ../Data/DMPK/dmpk_NC_000019.fasta output.txt
  ```
- generalized
  ```
  python3 generate_test_data.py
  ```

To generate graphs

- generalized
```
python3 Benchmarking_Graphs/generate_graphs.py
```

## Acknowledgements & individual contributions
- Nikhil:
- Annie:
- Avery:
- Andrea:
- Ben Langmead: the goat

---
2024 Andrea Cheng, Nikhil Choudhary, Avery Kuo, Annie Wang supervised by Dr. Ben Langmead
