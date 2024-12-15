import copy
import time
from classifier import *

class Validator:
    def __init__(self, featureSubset, classifierType, fileName):
        self._fileName = fileName
        self._featureSubset = featureSubset #list of features
        self._classfier = self.selectClassifier(classifierType, fileName)
        
        self._normDataSet = []
        for row in self._classfier._normFeatureSet:
            self._normDataSet.append(row)
        
        self._classSet = []
        for row in self._classfier._classSet:
            self._classSet.append(row)
    
    def selectClassifier(self, classifierType, fileName):
        match classifierType:
            case 1: #nearest neighbor
                myClassifier = Classifier()
                myClassifier.train(fileName)
                return myClassifier

    def testClassifier(self):
        start = time.process_time()

        #transposing is too slow, c++ logic time
        filterFeatureMatrix = []
        
        for row in self._normDataSet:
            filteredList = []
            
            for index in self._featureSubset: #index-1
                
                filteredList.append(row[index-1])
            filterFeatureMatrix.append(filteredList)
        
        numSuccess = 0.0
        for ignoreIndex in range(0, len(filterFeatureMatrix)):
            trainingMatrix = []
            for row in filterFeatureMatrix:
                trainingMatrix.append(row)

            leaveOutPoint = []
            for element in trainingMatrix[ignoreIndex]:
                leaveOutPoint.append(element)
            # print(leaveOutPoint)
          
            del trainingMatrix[ignoreIndex]

            tempClassSet = [] 
            # print(str(len(filterFeatureMatrix)))
            # print(str(len(self._classSet)))
            # print(str(ignoreIndex))
            for element in self._classSet:
                tempClassSet.append(element)  
            del tempClassSet[ignoreIndex]
            
            self._classfier.shallowTrain(trainingMatrix, tempClassSet) 
            testVal = int(self._classfier.test(leaveOutPoint))
           
            if testVal == int(self._classSet[ignoreIndex]):
                result = "TRUE"
                numSuccess += 1
            else:
                result = "FALSE"
            # print("Testing point " + str(ignoreIndex + 1) + " | Predicted Class: " + str(testVal) + " | Actual Class: " + str(int(self._classSet[ignoreIndex])) + "| Result: " + result)
        endTime = (time.process_time() - start)
        percentSucess = (numSuccess / len(self._classSet) ) * 100
        
        # print("testClassifier() " +str(endTime) + " Seconds")
        # print("Classification Accuracy: " + str(percentSucess) + "% | Time Spent: " + str(endTime) + " seconds")

        return percentSucess

                


