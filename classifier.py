import copy

class Classifier:
    def __init__(self):
        self._featureSet = []
        self._normFeatureSet = []
        self._classSet = []

    @staticmethod
    def normalizeData(dataSet):
        normalizedSet = []
        transposed = [[row[i] for row in dataSet] for i in range(len(dataSet[0]))]
        for featureCol in transposed:
            tempList = []
            dataMax = max(featureCol)
            dataMin = min(featureCol)
            for data in featureCol:
                newData = (data-dataMin)/(dataMax-dataMin)
                tempList.append(newData)
            normalizedSet.append(tempList)
        return normalizedSet           
            
    def train(self, fileName): #input training data into vectors
        #https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/
        with open(fileName, 'r') as file:
            for line in file:
                strToFloatList = [float(item) for item in line.split()]
                self._classSet.append(strToFloatList[0])
                self._featureSet.append(strToFloatList[1:])
        self._featureSet = list(filter(None, self._featureSet))     
        self._classSet = list(filter(None, self._classSet))    
        self._normFeatureSet = copy.deepcopy(self.normalizeData(self._featureSet))


    def test(self, testPoint): #find distance to all points, return label of closest
        closestPoint = 0
        for allPoints in self.featureSet:
            if(closestPoint > self.distance(allPoints, testPoint)):
                pass

    @staticmethod
    def distance(startPoint, endPoint): #returns euclidean distance between two points
        sum = 0
        for i in range(0,len(startPoint)): #loop through all features
            sum += (endPoint[i]-startPoint[i])**2
        return sum**0.5



#training instances are from 
#compute euclidean distance from training points
#return the class label of the nearest training point