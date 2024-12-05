from problemGraph import *

print("""Welcome to Nolan's Feature Selection Algorithm.\n""")
numFeatures = int(input("Please enter total number of features: "))
algoType = input("""\nType the number of the algorithm you want to run.\n
        (1) Forward Selection
        (2) Backward Selection
        (3) Nolan's Special Algorithm\n\t:""")


myGraph = Graph(numFeatures)
myGraph.test()
