###STILL NEED ARRAY CODE IN FILE
#Trying out a scatter plot to visualize the data because imshow
#is having a hard time with showing the very limited numbers of changes

#Here I'm plotting dots at grid locations where the array has a 1 (a seq change)

#the locations of interest (worth plotting) are those sites where a 1 is.
locations_to_plot = np.where(seq_array==1)
print locations_to_plot

#locations_to_plot have a coordinate location within the array
#the current array is 113 rows by 303 columns
#interestingly, the locations are represented as (y,x), when we'd rather have (x,y)
#to deal with this, we assign all the y coords and all the x coords to their own
#variables that then we can plot

ycoords = locations[0]
xcoords = locations[1]
plt.scatter(xcoords,ycoords)
plt.savefig("trialIHNfig.pdf") #saving to desktop right now.

#fig, data_image = subplots(figsize=(20, 20))
#data_image = plt.imshow(seq_array, interpolation = 'nearest', aspect= "auto" , cmap = color_map, norm=norm)
locations = np.where(seq_array==1)
ycoords = locations[0]
xcoords = locations[1]
plt.scatter(xcoords,ycoords)
plt.savefig("trialIHNfig.pdf")
#pyplot.show()
