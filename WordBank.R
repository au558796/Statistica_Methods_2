# can we predict vocabulary size from age?
data = read.delim("wordbankdata.csv", sep = ',')
model = lm (production ~ age, data)
summary(model)
#Call:
#lm(formula = production ~ age, data = data)

#Residuals:
 # Min      1Q  Median      3Q     Max 
#-589.22 -101.34    1.28  119.41  394.86 

#Coefficients:
 # Estimate Std. Error t value Pr(>|t|)    
#(Intercept) -577.398     34.567  -16.70   <2e-16 ***
 # age           36.231      1.331   27.21   <2e-16 ***
  #---
  #Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

#Residual standard error: 168.3 on 998 degrees of freedom
#Multiple R-squared:  0.4259,	Adjusted R-squared:  0.4254 
#F-statistic: 740.5 on 1 and 998 DF,  p-value: < 2.2e-16

data$mom_ed = ordered(data$mom_ed, levels = c("Primary", "Secondary", "Some College", "Graduate"))
model = lm(production ~ age + gender + mom_ed + comprehension, data = data)
summary(model)


