# Geography and host species shape the evolutionary dynamics of U genogroup infectious hematopoietic necrosis virus.

###### Black A<sup>1,3</sup>, Breyta R<sup>2,4</sup>, Bedford T<sup>1,3</sup>, and Kurath G. 2016<sup>2,4</sup>.

<sub><sup><sup>1</sup>Department of Epidemiology, University of Washington, Seattle, WA, USA, <sup>2</sup>U.S. Geological Survey, Western Fisheries Research Center, Seattle, WA, USA, <sup>3</sup>Vaccine and Infectious Disease Division, Fred Hutchinson Cancer Research Center, Seattle, WA, USA, <sup>4</sup>Cary Institute for Ecosystems Studies, Millbrook, NY, USA.</sub></sup>


## Abstract

Infectious hematopoietic necrosis virus (IHNV) is a negative-sense RNA virus that infects wild and cultured salmonids throughout the Pacific Coastal United States and Canada, from California to Alaska. Although infection of adult fish is usually asymptomatic, juvenile infections can result in high mortality events that impact salmon hatchery programs and commercial aquaculture. We used epidemiological case data and genetic sequence data from a 303nt portion of the viral glycoprotein gene to study the evolutionary dynamics of U genogroup IHNV in the Pacific Northwestern United States from 1971 to 2013. We identified 114 unique genotypes among 1219 U genogroup IHNV isolates representing 619 virus detection events. We found evidence for two previously unidentified, broad subgroups within the U genogroup, which we designated ‘UC’ and ‘UP’. Epidemiologic records indicated that UP viruses were detected more frequently in sockeye salmon (Oncorhynchus nerka) and in coastal waters of Washington and Oregon, whereas UC viruses were detected primarily in Chinook salmon (_O. tshawytscha_) and steelhead trout (_O. mykiss_) in the Columbia River Basin, which is a large, complex watershed extending throughout much of interior Washington, Oregon, and Idaho. These findings were supported by phylogenetic analysis and by FST. Ancestral state reconstruction indicated that early UC viruses in the Columbia River Basin initially infected sockeye salmon but then emerged via host shifts into Chinook salmon and steelhead trout sometime during the 1980s. We postulate that the development of these subgroups within U genogroup was driven by selection pressure for viral adaptation to Chinook salmon and steelhead trout within the Columbia River Basin.


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
