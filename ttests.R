setwd("C:/Users/Dana/Desktop/SEMESTER 1/EXPERIMENTAL METHODS/2016-Cognitive Science/2016-Experimental Methods/Data for exercises/Everything RStudio")
brain.Data=BrainSize

t.test(BrainWeight~Gender, data= brain.Data, paired=FALSE)
t.test(brain.Data$BrainWeight,brain.Data$HeadSize, paired = FALSE)

cor.test<-lm(BrainWeight~Gender, data = brain.Data)
cor.test
plot(cor.test)


