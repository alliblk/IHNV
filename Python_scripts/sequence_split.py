#Import FASTA file as a list of strings, where title and sequence are separate arguments
fasta_list = open ("UEvents_Date_sort_only.txt").read().splitlines()

#Create a new FASTA file with the same titles, but with only the first portion of the seq
#Iterate through the list printing the full title (args 0,2,4...i)
#but only characters 0-152 for the sequence string.

#try making a new list, then IF argument starts with > append whole argument
#else append arg[0:152]

cropped_seq_listA = []
for argument in fasta_list:
	if argument.startswith(">"):
		cropped_seq_list.append(argument)
	else:
		cropped_seq_list.append(argument[0:152])
fasta_outA = ("\n").join(cropped_seq_listA)
		
#This makes a list in the same format of the fasta_list above, where the title is an
#argument, then the cropped sequence is the next argument etc.
#I then edited the square brackets out and replaced commas with newlines in a text editor.
#NEED TO MAKE THE CODE ACTUALLY OUTPUT THE FASTA FILE AS I'D LIKE IT....
#DO LATER, JUST GET TREES RUNNING RIGHT NOW.

#Repeat in order to get the second half of the sequence, again with the full FASTA titles

cropped_seq_listB = []
for argument in fasta_list:
	if argument.startswith(">"):
		cropped_seq_listB.append(argument)
	else:
		cropped_seq_listB.append(argument[152:])
fasta_outB = ("\n").join(cropped_seq_listB)