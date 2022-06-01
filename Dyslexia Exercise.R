install.packages("caret")
install.packages("e1071")
library(caret)
library(e1071)

#split text based on "task"
d.Text=dyslexia[dyslexia$Task=="Text",]
d.Words=dyslexia[dyslexia$Task=="Words",]
d.non.Words=dyslexia[dyslexia$Task=="Non-Words",]

#make a logistic regression with one predictor(baseline)
m1=glm(Diagnosis~Mistakes, data=d, family="binomial")
m1.Sum=summary(m1)

#datafram
d=dyslexia

#make a vector which predicts "response"
predictions=predict(m.non.Words,type="response")

#if 'response' is <.5, label as 'noDyslexia', vice versa
predictions
predicted_diagnosis=ifelse(predictions<.5,"noDyslexia","Dyslexia")
predicted_diagnosis

#make a matrix to see how accurate predictions of diagnosis are
d.Matrix=caret::confusionMatrix(predicted_diagnosis,d$Diagnosis, positive="Dyslexia")
d.Matrix

#multiple regression to test different hypothesis of predictors
m.Words=glm(Diagnosis~SyllableN, data=d.Words,family = "binomial")

#View coefficients, chisq, p-values, fischer values
summary(m.Words)
anova(m.Words,test = "Chisq")

m.Text=glm(Diagnosis~SyllableN+Duration, data=d.Text,family = "binomial")
summary(m.Text)
anova(m.Text, test = "Chisq")

m.non.Words=glm(Diagnosis~SyllableN+SyllablePerVoicedSecond,data=d.non.Words,family = "binomial")
summary(m.non.Words)
anova(m.non.Words, test = "Chisq")

caret::confusionMatrix(predicted_diagnosis,d.non.Words$Diagnosis,positive="Dyslexia")
