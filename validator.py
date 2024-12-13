import copy
from classifier import *

class Validator:
    def __init__(self, featureSubset, classifierType, fileName):
        self._fileName = fileName
        self._featureSubset = featureSubset #list of features
        self._classfier = self.selectClassifier(classifierType, fileName)
        self._normDataSet = copy.deepcopy(self._classfier._normFeatureSet)
        self._classSet = copy.deepcopy(self._classfier._classSet)
        print(self._classSet)
    
    def selectClassifier(self, classifierType, fileName):
        match classifierType:
            case 1:
                myClassifier = Classifier()
                myClassifier.train(fileName)
                return myClassifier

    def testClassifier(self):
        print("Validating Classifier...")
        numSuccess = 0

        #features to keep -> features to remove
        allFeatures = list(range(1, len(self._normDataSet[0]) + 1 ))
        featureRemoveList = [x for x in allFeatures if x not in self._featureSubset]

        #remove features not in keep list
        transposed = [[row[i] for row in self._normDataSet] for i in range(len(self._normDataSet[0]))]
        for i in reversed(range(len(featureRemoveList))):
            del transposed[featureRemoveList[i]-1]
        filterFeatureMatrix = [[row[i] for row in transposed] for i in range(len(transposed[0]))]  

        #save classSet
        for ignoreIndex in range(0, len(filterFeatureMatrix)):
            trainingMatrix = copy.deepcopy(filterFeatureMatrix)
            leaveOutPoint = copy.deepcopy(trainingMatrix[ignoreIndex])
            del trainingMatrix[ignoreIndex]
            tempClassSet = copy.deepcopy(self._classSet)      
            del tempClassSet[ignoreIndex]
            self._classfier.shallowTrain(trainingMatrix, tempClassSet)                
            testVal = int(self._classfier.test(leaveOutPoint))
            if testVal == int(self._classSet[ignoreIndex]):
                result = "TRUE"
                numSuccess += 1
            else:
                result = "FALSE"
            print("Testing point " + str(ignoreIndex + 1) + " | Predicted Class: " + str(testVal) + " | Actual Class: " + str(int(self._classSet[ignoreIndex])) + "| Result: " + result)
        percentSucess = (numSuccess / len(self._classSet) ) * 100
        print("Classification Accuracy: " + str(percentSucess) + "%")

        #reset self._normDataSet
        # self._classfier.train(self._fileName)

                


