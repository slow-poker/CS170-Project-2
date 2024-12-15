import copy
import sys
import math
import time

class Classifier:
    def __init__(self):
        self._featureSet = []
        self._normFeatureSet = []
        self._classSet = []
        self._normVars = []

    def normalizeData(self, dataSet):
        start = time.process_time()

        normalizedSet = []
        transposed = [[row[i] for row in dataSet] for i in range(len(dataSet[0]))]
        for featureCol in transposed:
            tempList = []
            dataMax = max(featureCol)
            dataMin = min(featureCol)
            avg = sum(featureCol) / len(featureCol)
            self._normVars.append([dataMax, dataMin, avg])
            for data in featureCol:
                newData = (data-dataMin)/(dataMax-dataMin)
                tempList.append(newData)
            normalizedSet.append(tempList)
        tempMatrix = [[row[i] for row in normalizedSet] for i in range(len(normalizedSet[0]))]
        
        endTime = (time.process_time() - start)
        # print("normalizeData() " + str(endTime) + " Seconds")
        return tempMatrix       

    def shallowTrain(self, normMatrix, classSet): #only for use in Validator testClassifier()
        self._normFeatureSet.clear()
        for row in normMatrix:
            self._normFeatureSet.append(row)

        self._classSet.clear()
        # print(str(len(classSet)))
        for row in classSet:
            self._classSet.append(row)
            
    def train(self, fileName): #input training data into vectors
        #https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/
        with open(fileName, 'r') as file:
            for line in file:
                strToFloatList = [float(item) for item in line.split()]
                self._classSet.append(strToFloatList[0])
                self._featureSet.append(strToFloatList[1:])
                # print(len(self._featureSet[0]))
        # print(self._classSet)
        # print(self._featureSet[0])
        self._featureSet = list(filter(None, self._featureSet))     
        # self._classSet = list(filter(None, self._classSet))    
        # print(str(len(self._classSet)))

        norm = self.normalizeData(self._featureSet)
        for row in norm:
            self._normFeatureSet.append(row)

    def test(self, testPoint): #find distance to all points, return label of closest
        # for col in range(len(self._featureSet[0])):
        #     featureMax = self._normVars[col][0]
        #     featureMin = self._normVars[col][1]
        #     avg = self._normVars[col][2]
        #     for index, data in enumerate(testPoint):
        #         newData = 0
        #         if featureMax == featureMin:
        #             newData = 0
        #         else:
        #             newData = (data-featureMin)/(featureMax-featureMin)
        #         testPoint[index] = newData
        
        closestPointDist = sys.maxsize
        index = 0
        indexOfClosestPoint = 0
        for allPoints in self._normFeatureSet:
            # print(testPoint)
            # print(allPoints)
            testDistance = self.distance(allPoints, testPoint)
            if(closestPointDist > testDistance):
                closestPointDist = testDistance
                indexOfClosestPoint = index
                # print("New closest point distance: " + str(testDistance) + "| Point Class: " + str(self._classSet[indexOfClosestPoint]))
            index += 1
        return self._classSet[indexOfClosestPoint]

    @staticmethod
    def distance(startPoint, endPoint): #returns euclidean distance between two points
        sum = 0
        for i in range(0,len(startPoint)): #loop through all features
            sum += pow((endPoint[i]-startPoint[i]), 2)
        return math.sqrt(sum)