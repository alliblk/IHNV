
#######################################
#PART B, sequence comparison to a reference sequence
#If the reference and the sequence match at a site, a 0 is assigned,
#If the reference and the sequence DO NOT match at a site, 1 is assigned
#Output is a string of 0s and 1s the length of the nt sequence
ref = "BBAA"

seqA = "AAAA"
seqB = "AAAB"
seqC = "ABBB"

sequences = [seqA, seqB, seqC]

def compare_to_ref(seq):
	output = ""
	for (a,b) in zip(ref, seq):
		if a == b:
			output += "0"
		else:
			output += "1"
	print output

def walkthrough_seqs():
	for seq in sequences:
		compare_to_ref(seq)

#Should probably write each sequence line to a file so in the end
#I have a text file with a chronological and UC/UP ordered column site by site.
#Also then I'm not copying and pasting each output to my own text file...