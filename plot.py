from matplotlib import pyplot as plt
import matplotlib 
matplotlib.use('tkagg')

#make x and y axis from features
filename = "Titanic clean.txt"
feature1 = 2
feature2 = 1
dev_x = []
dev_y = []
classList = []
with open(filename, 'r') as file:
    for line in file:
        lineList = line.split()
        classList.append(float(lineList[0]))
        del lineList[0]
        dev_x.append(float(lineList[feature1 - 1]))
        dev_y.append(float(lineList[feature2 - 1]))



#normalize data
normDev_x = [(data-min(dev_x))/(max(dev_x)-min(dev_x)) for data in dev_x]
normDev_y = [(data-min(dev_y))/(max(dev_y)-min(dev_y)) for data in dev_y]

#point colors
colors = ['red' if groupNum == 1 else 'blue' for groupNum in classList]

#axis labels
plt.xlabel('Feature ' + str(feature1))
plt.ylabel('Feature ' + str(feature2))
plt.title(filename)

#plot
plt.scatter(normDev_x, normDev_y, c=colors, s=80, edgecolors='black')
plt.show(block=True)