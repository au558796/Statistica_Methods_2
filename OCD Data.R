setwd("C:/Users/Dana/Desktop/METHODS II/CLASS EXERCIZES")
ocdData<-read.delim("OCD.dat",header= TRUE)
#install.packages("ggplot2")
#install.packages("WRS", repos = "http://R-Forge.R-project.org");#install.packages("mvnormtest");#install.packages("mvoutlier")
library("car");library("ggplot2");library("MASS");library("mvoutlier");library("mvnormtest");library(pastecs); library(reshape)
library("tidyr")
#library(WRS) "there is no package called "WRS"

#making column (variable) in data a factor and renaming headers (labels)
ocdData$Group<-factor(ocdData$Group, levels = c("CBT","BT","No Treatment Control"), labels = c("CBT","BT","NT"))
  
#scatterplot for thoughts vs. actions by treatment group
ggplot(data = ocdData, aes(x=Actions, y=Thoughts))+
  geom_point()+
  labs(x= "Obsession Related Actions", y="Obsession Related Thoughts", title= "Actions vs. Thoughts")+
  geom_smooth(method = lm)+
  facet_grid(.~Group)

#bar graph for treatment group vs. number of incidents for thoughts and actions
  #DONT KNOW HOW TO MEASURE BOTH ACTIONS AND THOUGHTS ????
ggplot(data = ocdData, aes(x=Group, y=Actions))+
  geom_bar(stat = "summary", fun.y = mean)

#descriotive statistics about actions and thoughts for different groups 
by(ocdData$Actions, ocdData$Group, stat.desc, basic = FALSE)
by(ocdData$Thoughts, ocdData$Group, stat.desc, basic = FALSE)  

#checking for covariance
by(ocdData[,2:3], ocdData$Group, cov)
#variance ratio threshold = 2, ratio of largest to smallest variance

#shapiro test for multivariate normality
  #subsetting data by group
cbt<- t(ocdData[1:10, 2:3])
bt<- t(ocdData[11:20, 2:3])
nt<- t(ocdData[21:30, 2:3])
#t is transpose, which makes columns into rows, and participants into columns
mshapiro.test(cbt)
mshapiro.test(bt)
mshapiro.test(nt)
#is p value is less than .05, then data deviate from multivariate normality

#checking for outliers
aq.plot(ocdData[,2:3])

#deleting outliers
new_ocdData<- ocdData[-26,]
#re-doing multivariance test
cbt<- t(new_ocdData[1:10, 2:3])
bt<- t(new_ocdData[11:20, 2:3])
nt<- t(new_ocdData[21:30, 2:3])

mshapiro.test(cbt)
mshapiro.test(bt)
mshapiro.test(nt)
#last one does work, figure out how to delete row and still run shapiro test

#variable with both actions and thoughts
outcome<- cbind(ocdData$Actions, ocdData$Thoughts)

model1<- manova(outcome ~ Group, data=ocdData)
model1
summary(model1)

#summary(model, intercept= TRUE, test= "Wilks"/"Hotelling"/"Roy")


#discriminant analysis
newModel<- lda(Group~ Actions + Thoughts, data = ocdData)
newModel
summary(newModel)

