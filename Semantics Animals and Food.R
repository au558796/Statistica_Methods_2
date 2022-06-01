Animals <- read.csv("C:/Users/Dana/Desktop/SEMESTER 1/COGNITION AND COMMUNICATION/Everything Python/Animals.csv")

library(ggplot2)

ggplot(Animals,aes(Animals$word_nr,Animals$distance))+
  geom_point()+
  geom_line()

plot(Animals$distance,Animals$time)


Food=read.csv("Food.csv")

ggplot(Food, aes(Food$word_nr,Food$distance))+
  geom_point()+
  geom_line()

ggplot(Animals, aes(Animals$word_nr, Animals$cumulative))+
  geom_point()+
  geom_line()+
  geom_text(label=Animals$word)

ggplot(Food,aes(Food$word_nr, Food$cumulative))+
  geom_point()+
  geom_line()+
  geom_text(label=Food$word)

