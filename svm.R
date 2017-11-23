library("e1071")


setwd("/home/long/TTU-SOURCES/software-verification")

training <- read.csv("trace-training.csv", header = TRUE)

attach(training)

x <- subset(training, select=-mul)
x = x[1:(nrow(x)-2),]
y <- mul[1:(length(mul)-2)]

y = as.factor(y)
dat = data.frame(x, y)

svm_model <- svm(y ~ ., data=dat, kernel="linear", cost=10, scale = FALSE)
summary(svm_model)


xtest = x[(nrow(x)-1):nrow(x), ]
ytest = mul[(length(mul)-1): length(mul)]
ytest = as.factor(ytest)

testdat = data.frame(xtest, mul=ytest)
ypred = predict(svm_model, testdat)

confusion_matrix = table(predict = ypred , truth = testdat$mul)


