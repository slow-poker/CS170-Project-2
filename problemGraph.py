#make a graph
#make a queue
#
#start node
#create nodes with start node as parent
#push them to a linked list
#
import random
from validator import *

class Node: 
    def __init__(self, data):
            self.data = []
            if data != None:
                 self.data = data.copy()
            self.child = None
            self.parent = None
            self.accuracy = None
        
class Graph:
    def __init__(self, fileName):
         self.root = Node(None)
         self.numFeatures = self.colInFile(fileName)
         self.fileName = fileName

    @staticmethod
    def colInFile(fileName):
         with open(fileName, 'r') as file:
              line = file.readline()
              numCol = len(line.split()) - 1 #first row is class
              return numCol


    def evaluate(self, currNode):
     #    start = time.process_time()
        # currNode.accuracy = (int(random.uniform(0, 100) * 100))/100
        myValidator = Validator(currNode.data, 1, self.fileName)
        currNode.accuracy = myValidator.testClassifier()
     #    endTime = (time.process_time() - start)
        # print("Evaluation time: " + str(endTime))

    #for priority queue sorting key
    @staticmethod
    def orders_by_accuracy(Node):
         return Node.accuracy * -1

    #make children nodes, push them into priority queue, parent and child point to each other
    def expand(self, parentNode):
        start = time.process_time()
        #populate priority queue with children
        q = []
        for i in range(1, self.numFeatures + 1):
            if i in parentNode.data:
                 continue
            childNode = Node(parentNode.data)
            childNode.data.append(i)
            self.evaluate(childNode)
            q.append(childNode)
            print("\tUsing feature(s) " + str(childNode.data) + " accuracy is " + str(childNode.accuracy) )       
        pq = sorted(q, key = self.orders_by_accuracy)            
        print("Feature set " + str(pq[0].data) + " was best, accuracy is " + str(pq[0].accuracy) + "%")
        #parent and best child point to each other
        pq[0].parent = parentNode
        parentNode.child = pq[0]
        endTime = (time.process_time() - start)
        print("Expansion time:  " + str(endTime) + "\n")
        
    def eliminate(self, parentNode):
        q = []
        for i in range(1, self.numFeatures+1):
            if i not in parentNode.data:
                 continue
            childNode = Node(parentNode.data)
            childNode.data.remove(i)
            self.evaluate(childNode)
            q.append(childNode)
            print("\tUsing feature(s) " + str(childNode.data) + " accuracy is " + str(childNode.accuracy) )       
        pq = sorted(q, key=self.orders_by_accuracy)
        if pq[0].data:
            print("\nFeature set " + str(pq[0].data) + " was best, accuracy is " + str(pq[0].accuracy) + "%\n")
        else:
             print("\nAn empty feature set was the best, accuracy is "+ str(pq[0].accuracy) + "%\n")

        #parent and best child point to each other
        pq[0].parent = parentNode
        parentNode.child = pq[0]
    

            
    