install.packages("ggplot2")

# open from library ggplot2
library(ggplot2)

# Load data from the perosnality test
data=read.delim("CogSciPersonality2016.txt")

# Lav Histogram (binwidth handlerom hvor store kolonnerne er)
# Ved at vælge binwidth kan du vælge hvor mange str du vil have i en kolonne
ggplot(data, aes(x = Shoe_size)) + geom_histogram(binwidth = 2)

# Exercise 1
# Make histograms:

ggplot(data, aes(x = Romberg_eyes_closed)) + geom_histogram(binwidth = 5)
mean(data$Romberg_eyes_closed)
sd(data$Romberg_eyes_closed)
median(data$Romberg_eyes_closed)

ggplot(data, aes(x = Tongue_twister_rt)) + geom_histogram(binwidth = 2)
mean(data$Tongue_twister_rt)
sd(data$Tounge_twister_rt)
median(data$Tongue_twister_rt)
     
ggplot(data, aes(x = Volume)) + geom_histogram(binwidth = 2)
mean(data$Volume)
sd(data$Volume)
median(data$Volume)

ggplot(data, aes(x = Hours_music)) + geom_histogram(binwidth = 2)
mean(data$Hours_music)
sd(data$Hours_music)
median(data$Hours_music)

# Discuss in pairs
# Problems w/ data
# Romberg eyes closed: the data after 120 sec. is an error (max 120 sec)
# Tounge twister: Data beneath 25 sec is error, isn't possible
# Volume: 
# Hours of music: More than 24 hours of music is very extreme



# adding a graphcal layer
by(data$Shoe_size, data$Gender, mean)
by(data$Shoe_size, data$Gender, summary)

install.packages("pastecs")
library(pastecs)

# Split shoe_size by gender and run stat.desc on each group
by(data$Shoe_size, data$Gender, stat.desc)

# Simpler way to summarize
by(data$Shoe_size, data$Gender, stat.desc, basic=F, norm=T)

# Install pastecs for stats.desc()
library(pastecs)

stat.desc(data$Shoe_size)
stat.desc(data$Hours_music)
median(data$Shoe_size)
median(data$Hours_music)

# Hvis du er i tvivl om by
?by(data$Hours_music, data$Gender, summary)

# Make a list

ea = list(40, 10, 40, 10)
#Vi får det samme median af samme kategorier. 

# Calculate standard error of the mean for shoe size
length(data$Shoe_size)
sd(data$Shoe_size)
sqrt(length(data$Shoe_size))

2.446465/7.874008

# Jotættere på 0 desto bedre, og da vi får 0,310 er vores mean reliable. 