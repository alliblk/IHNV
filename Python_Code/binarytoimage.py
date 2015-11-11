###############################
#EXPLANATION
#I need an array, which is a list of lists.
#Each sequence needs to be it's own list where the 0 and 1s are the arguments
# EG [0,1,1,0,0,0]
#This is the "inner list"
#Then you need a list of each of the inner lists. This is the outer list.
#EG [[0,1,1,0,0,0] , [0,1,1,0,0,0] , [0,1,1,0,0,0]]
#This array then needs to be transformed into specifically a NumPy array
#to allow the plotting functionality.

################################
#Import packages
#FOR PLOTTING INLINE IN IPYTHON NOTEBOOK
%matplotlib inline

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

################################
#OPEN FILE
seq_string_list = open("binaryIHNoutput_FDdate_sort_only.txt").read().splitlines()
#print seq_string_list[1:5]

################################
#CREATE ARRAY -> NUMPY ARRAY
outer_list = []
for seq in seq_string_list:
	character_list = list(seq)#turns the string into a list of the characters
	integer_list = map(int, character_list) #turn strings in character_list to integers
#	integer_list = [int(x) for x in character_list] #example of list comprehension
	outer_list.append(integer_list)
print outer_list[0:5]

#print outer_list[1]
seq_array = np.array(outer_list)
#print seq_array[0:5]

################################
#GRAPH ARRAY
#NOTE: if matrix data is sparse, use plt.spy (as done below)
#If matrix data are not sparse, probably better to do with imshow

seq_comp_image = plt.spy(seq_array, markersize=2, color="Black", mec="Black")
seq_comp_image.axes.get_yaxis().set_ticks([]) #ticks as empty list causes the axis to hide
plt.savefig("/Users/allisonblack/Desktop/seqcomp_FD_DateSortOnly.pdf") #may need to add in file path if not in pwd
