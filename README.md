# IHNVcode
This repo contains data and code used for evolutionary analysis of Infectious Hematopoietic Necrosis Virus.

Data Files:
There are 4 data files. Each are .txt files with fasta formatted sequences.
One file contains all 114 unique U genogroup sequence types detected within the study, plus an outgroup taxon.
One file contains sequences for all 619 U events, sorted by date.
There are two additional files with only UC events or only UP events.
The files contain aligned sequences. Each sequence is 303nt long.
Each taxon name contains the isolation year, the unique sequence identifier, the subgroup, and a random number so that no taxon names repeat in that order.


Analysis Pipeline:

Phylogenetic Inference
Coalescent phylogenies were inferred in BEAST using the All U events data, or the UC and UP events data separately, as input files.
Maximum Likelihood phylogenies were inferred using the 114 unique genotypes data with an M genotype outgroup sequence.

Sequence Alignment Figure
Two scripts are used to make the sequence alignment figure. IHNBinarySeqComparison.py takes a fasta format file as input, and returns binary code output (0's where nucleotides are the same, and 1's where nucleotides are different).
Then the binary code can be taken as an input file into binarytoimage.py. The output will be a pdf where 1's are colored black, and 0's are left white.

Clock Plot
Maximum likelihood trees for UC and UP events were loaded into Path-O-Gen, and textfiles with root-to-tip distances and sampling year were exported.
These textfiles are the input files for Rcode_PathOGendata.R which makes the clock plots.

Skyline Plots
Tracer was used to analyze BEAST .trees files for UC and UP events separately. Bayesian Skyline Reconstruction was performed in Tracer, and the data files were exported as .tsv
The .tsv files serve as input files for SkylinePlotCode.R




