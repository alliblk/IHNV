####



#Install appropriate packages
from matplotlib import mpl, pyplot
import numpy as np

#Import the binary sequences in the textfile as file to use in the plotting process.


#Try and black and white first, then see about how to colour (IE give
#SNPs in the UC diff colour than in the UP....

#make the black and white colour map
BWmap = mpl.colors.ListedColormap(['black','white'])

#Black represents the 1's, IE the site differences, therefore need to enforce all 1
#to be black on the color map. This can be done with setting of the bounds.
#position in the syntax is same as position in the colormap syntax IE bounds for
#black will be first here, then the bounds for white.
bounds = [1,0.1,0]
norm = mpl.colors.BoundaryNorm(bounds, BWmap.N)

#tell imshow to use the color map defined above to assign colors to values
image = pyplot.imshow(INFILE

#Export the image...jpeg, pdf? Not sure what the format would be: CHECK!
pyplot.show()
######################################
#FROM STACKOVERFLOW EXAMPLE
from matplotlib import mpl,pyplot
import numpy as np

# make values from -5 to 5, for this example
zvals = np.random.rand(100,100)*10-5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['blue','black','red'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap,norm=norm)

# make a color bar
pyplot.colorbar(img,cmap=cmap,
                norm=norm,boundaries=bounds,ticks=[-5,0,5])

pyplot.show()