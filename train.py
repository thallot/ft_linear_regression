import csv
import matplotlib.pyplot as plt
import numpy as np

def GetData(path):
    """ Recuppere les data du csv et forme une liste de couple (int,int) """
    dataConvert = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data_csv = list(reader)
    data_csv.pop(0)
    for data in data_csv:
        dataConvert.append(list(map(int, data)))
    return dataConvert

def GetAxes(data):
    """ Split la liste en deux axes x et y pour le display """
    x = []
    y = []
    for element in data:
        x.append(int(element[0]))
        y.append(int(element[1]))
    return x, y

def EstimatePrice(a, b, x):
    """ Fonction qui représente la droite de la régression lineaire """
    return (a * x + b)

def Reduce(dataMax, dataMin, data):
    """ Réduit les données en gardant les proportionnalité """
    dataReduced = []
    for data in data:
        new = [(data[0] / (dataMax[0] - dataMin[0])), data[1]]
        dataReduced.append(new)
    return (dataReduced)

def DescentGradient(dataReduced, theta, learning, iterations):
    """ Détermine les theta pour avoir la droite la plus juste"""
    i = 0
    m = len(dataReduced)
    while i < iterations:
        tmpTheta = [0.0, 0.0]
        for data in dataReduced:
            cost = EstimatePrice(theta[1], theta[0], data[0]) - data[1]
            tmpTheta[0] += cost
            tmpTheta[1] += cost * data[0]
        theta[0] = theta[0] - learning * (1 / m) * (tmpTheta[0] / m)
        theta[1] = theta[1] - learning * (1 / m) * (tmpTheta[1] / m)
        i += 1
    return theta

def Display(data, theta):
    """ Affiche le nuage de point et la droite de regression lineaire """
    x, y = GetAxes(data)
    x = np.array(x)
    plt.scatter(x, y)
    y = theta[0] + theta[1]*x
    plt.plot(x, y, color = "g")
    plt.xlabel('Distance (miles)')
    plt.ylabel('Price ($)')
    plt.show()

def WriteTheta(theta):
    """Ecrit les theta dans un fichier externe """
    f = open("theta.txt", "w")
    f.writelines( [str(theta[0]), "\n", str(theta[1]),  "\n"])
    f.close()

if __name__ == '__main__':
    "" "Lis un jeu de données et détermine la droite de regression lineaire """
    data = GetData('data.csv')
    dataMax = max(data)
    dataMin = min(data)
    learning = 1
    iterations = 10000
    theta = [0, 0]
    dataReduced = Reduce(dataMax, dataMin, data)
    theta = DescentGradient(dataReduced, theta, learning, iterations)
    theta[1] = (theta[1] / (dataMax[0] - dataMin[0]))
    print("y =", round(theta[0], 2), "* x", round(theta[1], 2))
    WriteTheta(theta)
    Display(data, theta)
