
### Pangenome Query Optimization using Wheeler Graphs
Repository for Computational Genomics Fall 2024, Group 4d

#### Writeup (link later)
#### Abstract
Reference bias leads to misalignment or exclusion of reads and incomplete identification of variants, and the scalability of existing pangenome representations remains a significant computational challenge. Here we investigate the utility of Wheeler graphs—a novel graph structure characterized by path coherence and efficient querying capabilities—for storing and querying pangenomes. Benchmarking against traditional methods, we observed that the Wheeler graph achieved competitive query efficiency while reducing memory requirements in the CTG-repeat-heavy DMPK pangenome. Additionally, its ability to compactly store repetitive sequences demonstrated promise for scalability in large-scale genomic datasets. Our findings suggest that Wheeler graphs are a viable alternative to traditional data structures for pangenome representation, offering improved computational efficiency and scalability, particularly for variant detection in complex genomic regions.

#### Reproducibility
Each indexing representation (K-mer_Index, SuffixTree, DeBruijn_Graph) can be accessed through its respective folder along with instructions to run the code. The Wheeler graph representation is generated through the Debruijn implementation and then fed through the Wheelie algorithm.

#### Ref
Andrea Cheng, Nikhil Choudhary, Avery Kuo, Annie Wang supervised by Dr. Ben Langmead
