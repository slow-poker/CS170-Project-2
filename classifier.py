
class Classifier:
    def __init__(self):
        self._featureSet = [[]]

    @property
    def featureSet(self):
        return self._featureSet

    def train(self, fileName): #input training data into vectors
        #https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/
        with open(fileName, 'r') as file:
            for line in file:
                strToFloatList = [float(item) for item in line.split()]
                self._featureSet.append(strToFloatList)
        self._featureSet = list(filter(None, self._featureSet))       
        
        # #test
        # num=1
        # for i in self._featureSet:
        #     print(i)
        #     print(str(num))
        #     num += 1

    def test(): #
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