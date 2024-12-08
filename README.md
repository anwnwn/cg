
### Pangenome Query Optimization using Wheeler Graphs
Repository for Computational Genomics Fall 2024, Group 4d

#### Writeup 
Located in the Documents directory 

#### Abstract
Reference bias, the tendency for genetic analyses to favor sequences similar to a single linear reference genome, often leads to the misalignment or exclusion of reads, resulting in incomplete variant detection and biased genomic studies. Pangenomes address these limitations by capturing the full spectrum of genetic diversity within a species, incorporating core, accessory, and variant sequences to enable more comprehensive and equitable analyses. However, existing approaches for pangenome analysis, such as multiple sequence alignment, k-mer indexes, suffix trees, de Bruijn graphs, and variation graphs, exhibit distinct trade-offs in scalability, storage efficiency, and query performance. To facilitate greater adoption of pangenomes over traditional linear reference genomes, there is a critical need for novel data structures that can efficiently store and query the vast diversity of genetic information while maintaining computational feasibility at scale. This paper explores the application of Wheeler Graphs to pangenome storage and querying, leveraging their path coherence and compression properties. Wheeler Graphs allow for efficient pattern matching and storage by encoding repetitive sequences and their variations in a succinct, ordered structure. Using a dataset that includes 14 variants of the DMPK gene, a gene with clinically significant repeat expansions, we benchmark the Wheeler Graph implementation against custom implementations of k-mer indexes and suffix trees. Results demonstrate that Wheeler Graphs achieve superior storage efficiency and competitive query performance while significantly reducing memory usage. These findings position Wheeler Graphs as a promising framework for scalable pangenome analysis, paving the way for more inclusive and accurate genomic studies.


#### Reproducibility
Each indexing representation (K-mer_Index, SuffixTree, DeBruijn_Graph) can be accessed through its respective folder along with instructions to run the code. The Wheeler graph representation is generated through the Debruijn implementation and then fed through the Wheelie algorithm.

#### Ref
Andrea Cheng, Nikhil Choudhary, Avery Kuo, Annie Wang supervised by Dr. Ben Langmead

### Individual Contributions

Nikhil:
Annie:
Avery:
Andrea:
