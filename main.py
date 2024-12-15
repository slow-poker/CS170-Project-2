from problemGraph import *

# Group: Nolan Vernon - nvern003
# - Small Dataset Results:
# - Forward: Feature Subset: {3,5}, Acc: 92.0%
# - Backward: Feature Subset: {2, 3, 4, 5} Acc: 83.0%
# - Large Dataset Results:
# - Forward: Feature Subset: {1, 27}, Acc: 95.5%
# - Backward: Feature Subset: {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39}, Acc: 71.1%
# - Titanic Dataset Results:
# - Forward: Feature Subset: {2, 5}, Acc: 78.01%
# - Backward: Feature Subset: {2}, Acc: 78.01%

print("""Welcome to Nolan's Feature Selection Algorithm.\n""")
algoType = input("""\nType the number of the algorithm you want to run.\n
        (1) Forward Selection Quick End
        (2) Forward Selection Full Search
        (3) Backward Selection Quick End
        (4) Backward Selection Full Search\n\t:""")

myGraph = Graph("titanic clean.txt")
numFeatures = myGraph.numFeatures

if int(algoType) == 3 or int(algoType) == 4:
        #populate root features
        for i in range(1, numFeatures + 1):
                myGraph.root.data.append(i)
        myGraph.evaluate(myGraph.root)
        print("Using all features and \"random\" evaluation, I get an accuracy of " + str(myGraph.root.accuracy) + "%\n")

else:
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

        case 3:
                #backward selection quick end
                currNode = myGraph.root
                for i in range(0, numFeatures):
                        myGraph.eliminate(currNode)
                        currNode = currNode.child
                        if currNode.accuracy < currNode.parent.accuracy:
                                print("(Warning, Accuracy has decreased!)")
                                currNode = currNode.parent
                                break

        case 4:
                #backward selection full search
                currNode = myGraph.root
                bestNode = myGraph.root
                for i in range(0, numFeatures):
                        myGraph.eliminate(currNode)
                        currNode = currNode.child
                        if currNode.accuracy > bestNode.accuracy:
                                bestNode = currNode
                                print("Updated best feature set to: "+ str(bestNode.data) + " with an accuracy of " + str(bestNode.accuracy)+ "%\n")

if int(algoType) % 2 == 0:
        print("Finished search!! The best feature subset is "+ str(bestNode.data) + " which has an accuracy of " + str(bestNode.accuracy) + "%\n")
else:
        print("Finished search!! The best feature subset is "+ str(currNode.data) + " which has an accuracy of " + str(currNode.accuracy) + "%\n")
