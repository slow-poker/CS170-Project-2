from problemGraph import *
from searchAlgos import *

print("""Welcome to Nolan's Feature Selection Algorithm.\n""")
numFeatures = int(input("Please enter total number of features: "))
algoType = input("""\nType the number of the algorithm you want to run.\n
        (1) Forward Selection Quick End
        (2) Forward Selection Full Search
        (2) Backward Selection
        (3) Nolan's Special Algorithm\n\t:""")

myGraph = Graph(numFeatures)
myGraph.evaluate(myGraph.root)
print("Using no features and \"random\" evaluation, I get an accuracy of " + str(myGraph.root.accuracy) + "%\n")
print("Beginning search")

match int(algoType): 
        case 1:
                #forward selection quick end
                currNode = myGraph.root
                for i in range(0, numFeatures):
                        myGraph.expand(currNode)
                        currNode = currNode.child
                        if currNode.accuracy < currNode.parent.accuracy:
                                print("(Warning, Accuracy has decreased!)")
                                currNode = currNode.parent
                                break
                print("Finished search!! The best feature subset is "+ str(currNode.data) + " which has an accuracy of " + str(currNode.accuracy) + "%\n")
        
        case 2:
                #forward selection full search
                currNode = myGraph.root
                bestNode = myGraph.root
                for i in range(0, numFeatures):
                        myGraph.expand(currNode)
                        currNode = currNode.child
                        if currNode.accuracy > bestNode.accuracy:
                                bestNode = currNode
                                print("Updated best feature set to: "+ str(bestNode.data) + " with an accuracy of " + str(bestNode.accuracy)+ "%\n")
                print("Finished search!! The best feature subset is "+ str(bestNode.data) + " which has an accuracy of " + str(bestNode.accuracy) + "%\n")
