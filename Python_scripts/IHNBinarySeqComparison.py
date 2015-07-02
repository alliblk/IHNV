###############################
#PART A: import and read in the FASTA file
#import sys
fasta_infile = open("UEvents_Date_sort_only.txt",'r') #infile is a FASTA format file and a command line arg
fasta_list = fasta_infile.readlines()

#this readlines function will create a list where each argument is a string
#note that this means that titles (>XXX) are separate arguments from the sequences
#Super important then NOT TO REORDER THE LIST
#Probably better to make a dictionary so that these couplings don't get lost...
#try and get a dictionary way of doing this to work too...

##############################
sequences_only_list = [] #create a new list that will house the sequences only

for i in xrange(1, len(fasta_list),2): #syntax is xrange(start, end, increment)
	sequences_only_list.append(fasta_list[i].strip())

#print sequences_only_list

#######################
#Trevor's sequence comparison functions

#Function 1: this function takes in two arguments, the reference seq and a single comparator seq
#At each site in the sequence if the bases are the same, then a 0 is written to the output
#if a site has a different base between the ref and the seq, then 1 is written to the output
#The output is then a matrix of 0s and 1s of the same length as the nt sequence.
#Running this function will create a single pairwise comparison

def compare_to_ref(reference,seq):
	output = "" #define output as an empty string
	for (a,b) in zip(reference, seq):
		if a == b:
			output += "0"
		else:
			output += "1"
	output += "\n"
	return output #final output is a filled string, this can be assigned to a variable later
#note that returning the output allows you to gain access to it later on
#as long as you assign the called function to a saved variable

##########################
#WRITE THE OUTPUT TO A FILE
#Remember to create the file in the correct directory first
#final_output_file = open("binaryIHNoutput_FDdate_sort_only.txt", 'w')	
reference1 = sequences_only_list[0]
for seq in sequences_only_list[1:]:
	binary_output = compare_to_ref(reference1, seq)
	#final_output_file.write(binary_output) #only write the file once to avoid overwriting

