import numpy as np
import matplotlib.pyplot as plt
from kmeans import plot_k_means,get_simple_data,cost



def main():
    X = get_simple_data()

    costs = np.empty(10)
    costs[0] = None

    for k in range(1,10):
        c = plot_k_means(X,k)
        costs[k] = c
    
    plt.plot(costs)
    plt.title('cost vs K')
    plt.show()


main()