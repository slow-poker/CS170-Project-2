from classifier import *
from validator import *

myClassifier = Classifier()
trainingData = "small-test-dataset.txt"
myClassifier.train(trainingData)

featureSubset = [3, 5, 7]
classifierType = 1
myValidator = Validator(featureSubset, classifierType, trainingData)
myValidator.testClassifier()


