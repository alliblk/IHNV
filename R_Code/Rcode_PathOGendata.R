###INPUT FILES: all data exported as .txt from Path-O-Gen
getwd()
setwd("/Users/allisonblack/Desktop/Clock_Plots")
AllU = read.table("UEventsCLOCK_outgrp_RAxML.txt", header=T)
UC = read.table("UCEventsCLOCK_outgrp_RAxML.txt", header=T)
UP = read.table("UPEventsCLOCK_outgrp_RAxML.txt", header=T)

Udistances = AllU$distance
Udates = AllU$date

UCdistances = UC$distance
UCdates = UC$date

UPdistances = UP$distance
UPdates = UP$date

list(Udates)
###########################
#BASIC PLOTTING WITH LINEAR REGRESSION

#All U events with linear line and lowess line
plot(Udistances~Udates, xlim=c(1970,2020), 
     ylim = c(0,0.04), xlab="Sampling Year" , ylab="Root-to-Tip Divergence", col=c("black"), pch=16, main="U Events 1971-2013")
abline(lm(Udistances~Udates), col="red",lwd=3)
#lines(lowess(Udates,Udistances), col="red", lwd=5)

###UC and UP point OVERLAY

plot(UCdistances~UCdates,type="p",col="orange", pch=16, xlim=c(1970,2015),
     ylim = c(0,0.04), xlab="Sampling Year" , ylab="Root-to-Tip Divergence")
points(UPdistances~UPdates,col="light blue", pch=16)
abline(lm(UCdistances~UCdates), col="dark orange",lwd=3)
abline(lm(UPdistances~UPdates), col="light blue",lwd=3)
legend('topleft', inset=0.02,c("UP","UC"),fill=c("light blue","orange"),  bty = "n")
#####################################
par(mfrow=c(1,2))
par(mfrow=c(1,1))

#UC events with linear line and lowess line
plot(UCdistances~UCdates, xlim=c(1955,2020), xlab="Time",ylim=c(0,0.03) , ylab="Root-to-Tip Divergence", col=c("dark red"), pch=16, main="UC Events")
abline(lm(UCdistances~UCdates), col="black",lwd=2)
lines(lowess(UCdates,UCdistances), col="red", lwd=4)
summary(lm(UCdistances~UCdates))

#UP events with linear line and lowess line
plot(UPdistances~UPdates, xlim=c(1955,2020), xlab="Time" ,ylim=c(0,0.03), ylab="Root-to-Tip Divergence", col=c("dark blue"), pch=16, main="UP Events")
abline(lm(UPdistances~UPdates), col="black",lwd=2)
lines(lowess(UPdates,UPdistances), col="red", lwd=4)
summary(lm(UPdistances~UPdates))

###########################
#LINEAR REGRESSION AND SUMMARIES
summary(lm(Udistances~Udates))
summary(lm(UCdistances~UCdates))
summary(lm(UPdistances~UPdates))

###########################
#NON-LINEAR REGRESSION
#U events exponential model test
Uexpmod = lm(log(Udistances)~Udates)
plot(Uexpmod)
summary(lm(Uexpmod))

#####TRIAL STUFF
Upoly = lm(formula = Udistances ~Udates + I(Udates^2) + I(Udates^3))
summary(Upoly)

plot(log(Udistances)~Udates)
abline(lm(log(Udistances)~Udates))
summary(lm(log(Udistances)~Udates))
#UC EVENTS

plot(UCdistances~UCdates, pch=16, col=c("dark red"), ylim=c(0,0.03), xlim=c(1955, 2020))
abline(lm(UCdistances~UCdates))
lines (lowess(UCdates,UCdistances))
summary(lm(UCdistances~UCdates))
