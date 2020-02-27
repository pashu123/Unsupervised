import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def get_simple_data():
    ## D is the no. of dimensions
    D = 2
    ## s is distance by which various gaussian clouds are separated
    s = 4

    ### There are 3 differnet gaussian clouds with different means as given
    mu1 = np.array([0,0])
    mu2 = np.array([s,s])
    mu3 = np.array([0,s])

    N = 900
    X = np.zeros((N,D))

    ## Filling the points with normal random variables
    X[:300,:] = np.random.randn(300,D) + mu1
    X[300:600,:] = np.random.randn(300,D) + mu2
    X[600:,:] = np.random.randn(300,D) + mu3

    return X


def main():
    
    X = get_simple_data()

    Z = linkage(X,'ward')
    print(f'Z shape: {Z.shape}')

    plt.title("ward")
    dendrogram(Z)
    plt.show()

    Z = linkage(X,'single')
    plt.title("single")
    dendrogram(Z)
    plt.show()

    Z = linkage(X,'complete')
    plt.title("complete")
    dendrogram(Z)
    plt.show()






if __name__ == "__main__":
    main()