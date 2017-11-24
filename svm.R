library("e1071")


setwd("/home/long/TTU-SOURCES/software-verification")

training <- read.csv("trace-training.csv", header = TRUE)

#attach(training)

row_split_train_and_test = 8

x <- subset(training, select=-mul)
x = x[1:row_split_train_and_test,]
y <- mul[1:row_split_train_and_test]

y = as.factor(y)
dat = data.frame(x, y)

svm_model <- svm(y ~ ., data=dat, kernel="linear", cost=10, scale = FALSE)
summary(svm_model)


testdat = data.frame(training[(row_split_train_and_test+1):nrow(training), ])
testdat$mul = as.factor(testdat$mul)

ypred = predict(svm_model, testdat)

table(predict = ypred , truth = testdat$mul)


