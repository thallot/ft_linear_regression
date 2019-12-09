import csv
import matplotlib.pyplot as plt
import numpy as np

def GetData(path):
    """ Recuppere les data du csv et les insere dans des liste """
    distance = []
    prices = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data_csv = list(reader)
    data_csv.pop(0)
    for element in data_csv:
        distance.append(int(element[0]))
        prices.append(int(element[1]))
    return distance, prices

def LinearRegression(x, y):
    """ Détermine les theta de la fonction de la regression lineaire """
    n = np.size(x)
    # Creation des vecteurs x et y
    vector_x, vector_y = np.mean(x), np.mean(y)
    # Calcul la différence entre les vecteurs et et les nuages de point
    SS_xy = np.sum(y*x) - n*vector_y*vector_x
    SS_xx = np.sum(x*x) - n*vector_x*vector_x
    # Détermine les coefficients de theta
    theta_1 = SS_xy / SS_xx
    theta_0 = vector_y - theta_1*vector_x
    return(theta_0, theta_1)

def Display(x, y, theta):
    """ Affiche le nuage de point et la droite de regression lineaire """
    #Affiche les points
    plt.scatter(x, y)
    # Definie la fonction de la regression lineaire
    y_pred = theta[0] + theta[1]*x
    # Affiche la droite de regression lineaire
    plt.plot(x, y_pred, color = "g")
    # Affiche les labels des axes
    plt.xlabel('Distance (miles)')
    plt.ylabel('Prices ($)')
    plt.show()


def main():
    distance, prices = GetData("data.csv")
    x = np.array(distance)
    y = np.array(prices)
    theta = LinearRegression(x, y)
    print("Estimated coefficients:\nb_0 = {}\nb_1 = {}".format(theta[0], theta[1]))
    Display(x, y, theta)

if __name__ == "__main__":
    main()
