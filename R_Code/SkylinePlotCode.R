getwd()
setwd("/Users/alliblk/Desktop/Figure Data Files/Skyline Plots")

#Remember to remove title line from tsv file manually before 
#loading the data into R.
UCskyline = read.table("UC_BS10_skylineplotdata.tsv", header=T)
UPskyline = read.table("UP_BS10_skylineplotdata.tsv",header=T)

#set up plotting panels
par(mfrow=c(1,2))

#UP SKYLINE PLOT
plot(UPskyline$Median ~UPskyline$Time, type="l",  
     log="y", ylim=c(0.01,1000), #note log 0 is -inf, so need a value
     col="light blue", 
     ylab = expression(paste(italic("N"[e]),tau," ","(years)")),
     xlab= "Sampling Year",
     main = "UP",
     lwd=6)
#the line above will be covered by the polygon
#however this allows me to get the plot area, axes, labels
#etc that I want to have on the plot.

#make the polygon border vectors
UP_X = c(UPskyline$Time, rev(UPskyline$Time))
UP_Y = c(UPskyline$Lower,rev(UPskyline$Upper))

#plot the polygon
polygon(UP_X, UP_Y, border=NA, col="light blue")

#plot the skyline lines over top of the polygon
lines(UPskyline$Median ~UPskyline$Time, type="l",
      lwd=4, col="black")

#NOTE! PLOT THE BELOW LINES TO MAKE SURE THAT THE POLYGON IS 
#CORRECT, but then comment out for no borders.
#lines(UPskyline$Upper~UPskyline$Time, type ="l", 
#lwd=2, lty=2, col= "black")
#lines(UPskyline$Lower~UPskyline$Time, type ="l", 
#lwd=2, lty=2, col="black")

#UC Skyline Plot
plot(UCskyline$Median ~UCskyline$Time, type="l",  
     log="y", ylim=c(0.01,1000),
     col="orange",
     ylab = expression(paste(italic("N"[e]),tau," ","(years)")),
     xlab= "Sampling Year",
     main= "UC",
     lwd=4)

UC_X = c(UCskyline$Time, rev(UCskyline$Time))
UC_Y = c(UCskyline$Lower,rev(UCskyline$Upper))

#plot the polygon
polygon(UC_X, UC_Y, border=NA, col="orange")

#plot the skyline lines over top of the polygon
lines(UCskyline$Median ~UCskyline$Time, type="l",
      lwd=4, col="black")
#lines(UCskyline$Upper~UCskyline$Time, type ="l", 
#lwd=2, lty=2, col= "black")
#lines(UCskyline$Lower~UCskyline$Time, type ="l", 
#lwd=2, lty=2, col="black")
