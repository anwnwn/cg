
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
Generalized for both
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
- DMPK, write results to wheeler_output.txt:
```
python3 -m Wheeler_Graph.wheeler Data/DMPK Benchmarking_Files/output.txt wheeler_output.txt
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
Andrea referenced various sources to modify the implementation of the De Bruijn graph, used the Wheeler Graph Toolkit Package to convert the De Bruijn Graph into Wheeler graph structure, coded a pattern matching algorithm based on the Wheeler Graph Structure, then wrote various scripts to allow all parts of the implementation to be run seamlessly from one command line script. Avery built the k-mer index structure to represent pangenomes, investigated ways to detect variation, and created a variation detection algorithm for the structure based on past literature review. She developed benchmarking standards for all structures. Using these standards, she created scripts to generate benchmarking data and results from all three structures so they can all be run consistently with the same command line. Annie built the custom suffix tree structure to represent pangenomes and constructed the proprietary variation detection algorithm optimized for longer queries with variation nodes defined based on consensus definition. She also wrote substring processing scripts to determine and consolidate the data used for the benchmarking setup and iteratively processed the benchmarking results. Nikhil conducted prior literature review, investigated prior implementations and other methods to represent pangenomes, and assembled deliverables (i.e., writeup, references, slides). He also created the final visualizations and figures in the paper. We all assisted each other when we ran into bugs and discussed potential issues/solutions and the writeup. 


---
2024 Andrea Cheng, Nikhil Choudhary, Avery Kuo, Annie Wang supervised by Dr. Ben Langmead
