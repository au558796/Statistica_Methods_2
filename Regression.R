library(boot)
library(Rcmdr)
install.packages("car")
install.packages("QuantPsych")
library(car)
library(QuantPsych)
library(ggplot2)
qplot(x=Album.Sales.1$adverts,y=Album.Sales.1$sales,  geom="point")+
  labs(x="Adverts", y="Sales", title = "Advertisting vs. Sales")+
  geom_smooth(method=lm, color="Red")+
  theme_classic()

#run regression analysis

#statistics-fit models-linear regression

