
data = read.delim("Lacourse et al. (2001) Females.dat")


Model1 = glm(Suicide_Risk ~ Metal, data = data, family = binomial())

Model1Chi = Model1$null.deviance-Model1$deviance
Model1Chi

chidf= Model1$df.null-Model1$df.residual
chidf

chisq.prob = 1- pchisq(Model1Chi, chidf)
chisq.prob

R2.hl = Model1Chi/Model1$null.deviance
R2.hl

Model2 = glm(Suicide_Risk ~ Metal + Self_Estrangement + Marital_Status, data = data, family = binomial())
Model2

