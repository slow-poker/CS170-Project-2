from problemGraph import *

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
