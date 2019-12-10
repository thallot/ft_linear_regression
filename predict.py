import matplotlib.pyplot as plt

def GetTheta():
    theta = [0.0, 0.0]
    with open("theta.txt") as file:
        data = file.read()
        words = data.split()
        theta = [float(words[0]), float(words[1])]
    return (theta)

def GetInput(theta):
    nbr = input('Please enter en mileages\n')
    if not nbr.isnumeric():
        print('Please give a numeric value\n')
        GetInput(theta)
    else:
        nbr = round(float(nbr), 1)
        price = round(theta[1] * nbr + theta[0], 1)
        if price < 0:
            price = 0
        print('Price for {} miles is {}' .format(nbr, price))


if __name__ == '__main__':
    theta = GetTheta()
    print(theta[0], theta[1])
    GetInput(theta)
