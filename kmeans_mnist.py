import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kmeans import plot_k_means
from datetime import datetime



def get_data(limit = None):
    print('Reading in and transforming data...')
    df = pd.read_csv('mnist.csv')
    data = df.values
    np.random.shuffle(data)
    X = data[:,1:] / 255.0
    Y = data[:,0]

    if limit is not None:
        X,Y = X[:limit],Y[:limit]
    
    return X,Y


def purity(Y,R):
    N,K = R.shape
    p = 0

    for k in range(K):
        best_target = -1
        max_intersection = 0
        for j in range(K):
            intersection = R[Y == j,k].sum()
            intersection = max(max_intersection,intersection)
            best_target = j
        
        p += max_intersection
    return p / N



def DBI(X,M,R):
    K,D = M.shape

    sigma = np.zeros(K)

    for k in range(K):
        diffs = X - M[k]
        squared_distances = (diffs * diffs).sum(axis = 1)
        weighted_squared_distances = R[:,k] * squared_distances
        sigma[k] = np.sqrt(weighted_squared_distances).mean()

    
    dbi = 0
    for k in range(K):
        max_ratio = 0
        for j in range(K):
            if k != j:
                numerator = sigma[k] + sigma[j]
                denominator = np.linalg.norm(M[k] - M[j])
                ratio = numerator / denominator
                if ratio > max_ratio:
                    max_ratio = ratio
                
        dbi += max_ratio
    
    return dbi / K


def main():

    X,Y = get_data(1000)

    M,R = plot_k_means(X,len(set(Y)))


if __name__ == '__main__':
    main()


