#install.packages("ggplot2")

#The downloaded binary packages are in
#C:\Users\Dana\AppData\Local\Temp\Rtmp0Ony60\downloaded_packages
> 
 # load library 
  
#library("ggplot2")
#setwd("C:/Users/Dana/Desktop/SEMESTER 1/EXPERIMENTAL METHODS/")

#set working directory in sessions = swd = choose directory

#> setwd("C:/Users/Dana/Desktop/SEMESTER 1/EXPERIMENTAL METHODS/uni.au.dk dfs/2015-Cognitive Science")
# load data
#data = read.delim("CogSciPersonality2016.txt")

#ggplot (data,aes(x=Romberg_eyes_closed))+geom_histogram(bins=2)

#ggplot (data,aes(x=Romberg_eyes_closed))+geom_histogram(bins=2)

#ggplot (data,aes(x=Tongue_twister_rt))+geom_histogram(binwidth=2)

#summary("Tongue_twister_rt")

# functions that give 1 number 
#median() 
#mean()
#sd()
#nrow()


#summary()

#pastecs::stat.desc() - stat.desc - comes from (::) library pastects (must load library before use)

#stat.desc(basic = FALSE , norm = TRUE)

#by(data, splitby, function)
# split data, apply function to split, combine to summary
# takes data in data frame (shoe size), "split by" gender, factor, logical vector, give it a function "run on each set of data" could be mean, summary, etc

#plotting with ggplot



#ggplot(data , aes (x = Romberg_eyes_closed)) + geom_histogram(binwidth = 2)
 

#install.packages("pastecs")

#library(pastecs)

#by(data$Romberg_eyes_closed , data$Gender , stat.desc)

#by(data $ Shoe_size , data$ Gender , stat.desc)

# split shoe size by gender, run stat.desc on each group

# ggplot(data, aes (x=Shoe_size)) + geom_histogram(binwidth = 2)

#median(data$Finger_ratio)
#median(data$Ballon_balancing)

#finger_balloon = c(0.955,8.5)


#Theresa = data [data$Name == "Theresa ,"]

#T.bone = data [data$Name == "Theresa" ]

#data$Ballon_balancing [data$Name == "Theresa"]
#data$Finger_ratio [data$Name == "Theresa"]

#Theresa = c (data$Ballon_balancing [data$Name == "Theresa"], data$Finger_ratio [data$Name == "Theresa"])


