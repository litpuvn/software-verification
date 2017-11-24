library("e1071")


#setwd("/home/hoanglong/TTU-SOURCES/software-verification")

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

pred = predict(svm_model, testdat)

confusionMatrix = table(pred, testdat$mul)

a = confusionMatrix[2,2]
b = confusionMatrix[2,1]
c = confusionMatrix[1, 2]
d = confusionMatrix[1, 1]

precision = a / (a + c)
recall = a / (a + b)
fMeasure = 2*a / (2*a + b + c)
accuracy = (a + d) / (a + b + c +d)

message(paste("accuracy: ", accuracy, "; precision: ", precision, "; recall: ", recall, "; f-measure: ", fMeasure))
