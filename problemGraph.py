#make a graph
#make a queue
#
#start node
#create nodes with start node as parent
#push them to a linked list
#
import random

class Node: 
    def __init__(self, data):
            self.data = []
            self.data.append(data)
            self.child = None
            self.parent = None
            self.accuracy = None

    def __lt__(self, other):
        return self.accuracy < other.accuracy
        
class Graph:
    def __init__(self, numFeatures):
         self.root = Node(None)
         self.numFeatures = numFeatures
         self.pq = []

    @staticmethod
    def evaluate(currNode):
        currNode.accuracy = random.uniform(0.00, 100.00)

    #make children nodes, push them into priority queue, parent and child point to each other
    def expand(self, parentNode):
        for i in range(self.numFeatures + 1):
            childNode = Node(parentNode.data)
            childNode.data.append(i)
            self.evaluate(childNode)
            self.pq.append(childNode)
        self.pq.sort

    def test(self):
         self.expand(self.root)
         for i in range(self.numFeatures + 1):
            node = self.pq[i]
            print( str(node.accuracy) + "'%' accuracy using features: " + str(node.data))
         
    