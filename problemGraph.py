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
            self.data = list(filter(None, self.data)) #removes None from initialization
            self.child = None
            self.parent = None
            self.accuracy = None

    def __lt__(self, other):
        return self.accuracy < other.accuracy
        
class Graph:
    def __init__(self, numFeatures):
         self.root = Node(None)
         self.numFeatures = numFeatures

    @staticmethod
    def evaluate(currNode):
        currNode.accuracy = random.uniform(0.00, 100.00)

    #make children nodes, push them into priority queue, parent and child point to each other
    def expand(self, parentNode):
        #populate priority queue with children
        pq = []
        for i in range(1, self.numFeatures + 1):
            childNode = Node(parentNode.data)
            childNode.data.append(i)
            self.evaluate(childNode)
            pq.append(childNode)    
        pq.sort

        #parent and child point to each other
        pq[0].parent = parentNode
        parentNode.child = pq[0]
            
        #TEST
        for i in range(self.numFeatures):
            node = pq[i]
            print( str(node.accuracy) + "% accuracy using features: " + str(node.data))


    def test(self):
         self.expand(self.root)
         
         
    