setwd("C:/Users/Dana/Desktop/SEMESTER 1/EXPERIMENTAL METHODS/2016-Cognitive Science/2016-Experimental Methods/Data for exercises/Everything RStudio/CLASS EXERCIZES")
triangles <- read.delim("C:/Users/Dana/Desktop/SEMESTER 1/EXPERIMENTAL METHODS/2016-Cognitive Science/2016-Experimental Methods/Data for exercises/Everything RStudio/CLASS EXERCIZES/triangles.txt", header=FALSE)
install.packages("irr")
library(irr)

names(triangles)=c("Participant","Stimuli","Coder1","Coder2")
triangles$diff=(triangles$Coder1==triangles$Coder2)
sum(triangles$diff)*100/length(triangles$diff)

kappa2(triangles[c(3,4)],"unweighted")
