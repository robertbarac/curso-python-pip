import matplotlib.pyplot as plt
from random import random
from math import sqrt

def graficar_circunferencia():
    x_list = []
    y_list = []
    for i in range(1000):
        x = random()
        y = random()
        if sqrt(x**2 + y**2) <=1:
            x_list.append(x)
            y_list.append(y)
        
    plt.scatter(x_list, y_list)
    plt.savefig('circunferencia.png')
    
graficar_circunferencia()