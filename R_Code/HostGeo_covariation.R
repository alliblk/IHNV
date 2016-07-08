setwd("~/Desktop/Manuscript Data Files")

data = read.csv("HostGeoClade_predictors.csv")
data
is.factor(data$Geography)
#make contingency table to check correlation between host and geography
host_geo_table = table(data$Host, data$Geography)
host_geo_table

#Chi-square to test hypothesis that Geography and Host are independent
chisq.test(host_geo_table)
# p < 0.0001, reject null hypothesis that host and geography are independent

#Since host and geography are not independent, which predictor predicts clade better?

#first, see how the data will be codified by R
contrasts(data$Genogroup)
contrasts(data$Host)
contrasts(data$Geography)

#logistic model with host as the only predictor of genogroup
host_model = glm(Genogroup ~ Host, family='binomial' , data=data)
summary(host_model)
#exp(summary(host_model)$coef) 
#exp(confint(host_model))

#logistic model with geography as the only predictor of genogroup
geo_model = glm(Genogroup ~ Geography, family='binomial', data=data)
summary(geo_model)
#exp(summary(geo_model)$coef) 
#exp(confint(geo_model))

#logistic model with both geography and host in the model
hostANDgeo_model = glm(Genogroup ~ Geography+Host, family='binomial', data=data)
summary(hostANDgeo_model)

par(mfrow=c(3,1))
plot(fitted(host_model),residuals(host_model))
plot(fitted(geo_model),residuals(geo_model))
plot(fitted(hostANDgeo_model),residuals(hostANDgeo_model))
