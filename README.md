# IHNVcode

This repo contains data and code used for evolutionary analysis of Infectious Hematopoietic Necrosis Virus.

### Data Files

Data files are .txt files with fasta formatted sequences. 
The files contain aligned sequences. Each sequence is 303nt long.
Each taxon name contains the isolation year, the unique sequence identifier, the subgroup, and a random number so that no taxon names repeat in that order.
This repo contains the following data files:
* 114 unique U genogroup sequence types detected within the study, plus an outgroup taxon. (114UniqueSeqs.txt)[https://github.com/alliblk/IHNVcode/blob/master/MaxLikelihood/114UniqueSeqs.txt]
* All 619 U events, sorted by date. (AllUEvents.txt)[https://github.com/alliblk/IHNVcode/blob/master/BEAST/All_U_Tree/AllUEvents.txt]
* Additional files with only (UC events)[https://github.com/alliblk/IHNVcode/blob/master/BEAST/UC_tree/UC_events.txt] or only (UP events)[https://github.com/alliblk/IHNVcode/blob/master/BEAST/UP_tree/UP_events.txt] for use in ancestral state reconstruction.


### Analysis

##### Phylogenetic Inference

* Maximum Likelihood phylogenies were inferred in RAxML using the 114 unique genotypes data with an M genotype outgroup sequence.

* Coalescent phylogenies were inferred in BEAST using data for All U events, or UC/UP events separately.

##### Sequence alignment to determine lineage defining nt sites:

Two scripts are used to make the sequence alignment figure. (IHNBinarySeqComparison.py)[https://github.com/alliblk/IHNVcode/blob/master/Python_Code/IHNBinarySeqComparison.py] takes a fasta format file as input, and returns binary code output (0's where nucleotides are the same, and 1's where nucleotides are different).

Then the binary code can be taken as an input file into (binarytoimage.py)[https://github.com/alliblk/IHNVcode/blob/master/Python_Code/binarytoimage.py]. The output will be a pdf where 1's (nt sites that are distinct fron the reference sequence) are colored black, and 0's (same as reference sequence) are left white.

##### Clock Plots:

Maximum likelihood trees for UC and UP events were loaded into Path-O-Gen, and textfiles with root-to-tip distances and sampling year were exported.
These textfiles are the input files for (Rcode_PathOGendata.R)[https://github.com/alliblk/IHNVcode/blob/master/R_Code/Rcode_PathOGendata.R] which makes the clock plots.

##### Skyline Reconstruction:

Bayesian Skyline Reconstruction was performed in Tracer, and the data files were exported as .tsv files.

Plotting was performed in R using (SkylinePlotCode.R)[https://github.com/alliblk/IHNVcode/blob/master/R_Code/SkylinePlotCode.R]


##### Ancestral State Reconstruction

* XMLs for performing the ancestral state reconstruction analysis can be found in the (Ancestral_State_Recon)[https://github.com/alliblk/IHNVcode/tree/master/BEAST/Ancestral_State_Recon] file. There are 2 xmls, one for UC and one for UP. Note that these XMLs make use of .trees files generated under a standard coalescent analysis performed for UC and UP separately. See (UC_tree)[https://github.com/alliblk/IHNVcode/tree/master/BEAST/UC_tree] or (UP_tree)[https://github.com/alliblk/IHNVcode/tree/master/BEAST/UP_tree] for data and XMLs.
* Geographic traits (either CRB or coastal) for all 619 U taxa can be found in (GeoTraitMap_AllU.txt)[https://github.com/alliblk/IHNVcode/blob/master/BEAST/Ancestral_State_Recon/GeoTraitMap_AllU.txt]
* Host traits (chinook, non-dominant, mykiss, or nerka) for all 619 U taxa can be found in (HostSppTraitMap_AllU.txt)[https://github.com/alliblk/IHNVcode/blob/master/BEAST/Ancestral_State_Recon/HostSppTraitMap_AllU.txt]



