#try to make a dictionary with the fasta
#try out using biopython

from Bio import SeqIO
import sys
fasta_dictionary = SeqIO.index("UEvents_UC_UP_andDateSort.txt, "fasta")
print fasta_dictionary["1971_mG018U_UP_1"] #note key call doesn't feature ">"

#iterating over all values in fasta_dictionary
#first value is the reference (ref = "1971_mG018U_UP_1")
#then for the remaining values, I want to compare the base at character X
#in the string (site X) to the base at site X in the value of the reference.
#if the ref base != seq base, I want to print (or append) the key of that seq
#the the base of that seq to a list, with a tab delimiter between them
#EG ">" + fasta_dictionary[key] + "\t" + value(X).

ref_seq = fasta_dictionary["1971_mG018U_UP_1"] #ref seq is EARLIEST seq in this case
print len(ref_seq) #should be 303 for midG IHN seqs

#for all_values_minus_ref in dictionary:
#	if siteX in str(value) != siteX in ref

trait_site = int(55) #change to whichever site you want to look at.

#If you want just the site that are different from the references
for key, value in fasta_dictionary.items():
	if value[trait_site] != ref_seq[trait_site]:
		trait_map_outfile.write(">" + key + "\t" + value[trait_site])

#Or if you want base at all taxa, this is what I used.
for key, value in fasta_dictionary.items():
	print ">" + key + "\t" + value[trait_site]