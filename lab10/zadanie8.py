
import numpy as np
import matplotlib.pyplot as plt
import random as rd

def rzut(n):
    x = [rd.randint(1,6)+rd.randint(1,6) for x in range(10)]
    plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Wartości')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    # wyświatlanie siatki
    plt.grid(True)
    plt.show()

rzut(6)