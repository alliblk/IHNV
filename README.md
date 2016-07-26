# IHNVcode

This repo contains data and code used for evolutionary analysis of Infectious Hematopoietic Necrosis Virus.

### Data Files

Data files are .txt files with fasta formatted sequences. You can find them [here](https://github.com/alliblk/IHNVcode/tree/master/Data_files) 
The files contain aligned sequences. Each sequence is 303nt long.
Each taxon name contains the isolation year, the unique sequence identifier, the subgroup, and a random number so that no taxon names repeat in that order.
This repo contains the following data files:



### Analysis

##### Phylogenetic Inference

* Maximum Likelihood phylogenies were inferred in RAxML using the 114 unique genotypes data with an M genotype outgroup sequence.

* Coalescent phylogenies were inferred in BEAST using data for All U events, or UC/UP events separately.

##### Sequence alignment to determine lineage defining nt sites:

Two scripts are used to make the sequence alignment figure. [IHNBinarySeqComparison.py](https://github.com/alliblk/IHNVcode/blob/master/Python_Code/IHNBinarySeqComparison.py) takes a fasta format file as input, and returns binary code output (0's where nucleotides are the same, and 1's where nucleotides are different).

Then the binary code can be taken as an input file into [binarytoimage.py](https://github.com/alliblk/IHNVcode/blob/master/Python_Code/binarytoimage.py). The output will be a pdf where 1's (nt sites that are distinct fron the reference sequence) are colored black, and 0's (same as reference sequence) are left white.

##### Clock Plots:

Maximum likelihood trees for UC and UP events were loaded into Path-O-Gen, and textfiles with root-to-tip distances and sampling year were exported.
These textfiles are the input files for [Rcode_PathOGendata.R](https://github.com/alliblk/IHNVcode/blob/master/R_Code/Rcode_PathOGendata.R) which makes the clock plots.

##### Skyline Reconstruction:

Bayesian Skyline Reconstruction was performed in Tracer, and the data files were exported as .tsv files.

Plotting was performed in R using [SkylinePlotCode.R](https://github.com/alliblk/IHNVcode/blob/master/R_Code/SkylinePlotCode.R)


##### Coalescent Phylogenies and Ancestral State Reconstruction

The primary analysis is done on the full events dataset, [this repo here](https://github.com/alliblk/IHNVcode/tree/master/BEAST_fullData)

The secondary analysis is done on an equitably subsampled dataset. The ipython notebook for doing the subsampling [can be found here](https://github.com/alliblk/IHNVcode/blob/master/Python_Code/Equitable_Event_Subsampling.ipynb). The repo with the XMLs for the subsampled analysis can be found [here](https://github.com/alliblk/IHNVcode/tree/master/BEAST_subsampledData).



