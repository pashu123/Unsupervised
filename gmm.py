import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn


def gmm(X,K,max_iter = 200,smoothing=1e-2):

    N,D = X.shape
    M = np.zeros((K,D))
    R = np.zeros((N,K))
    C = np.zeros((K,D,D))
    pi = np.ones(K) / K

    for k in range(K):
        M[k] = X[np.random.choice(N)]
        C[k] = np.diag(np.ones(D))

    costs = np.zeros(max_iter)

    weighted_pdfs = np.zeros((N,K))

    for i in range(max_iter):

        for k in range(K):
            weighted_pdfs[:,k] = pi[k]*mvn.pdf(X, M[k], C[k])
            

        R = weighted_pdfs / weighted_pdfs.sum(axis=1, keepdims=True)

        for k in range(K):
            Nk = R[:,k].sum()
            pi[k] = Nk/N
            M[k] = R[:,k].dot(X) / Nk
            delta = X - M[k] # N x D
            Rdelta = np.expand_dims(R[:,k], -1) * delta # multiplies R[:,k] by each col. of delta - N x D
            C[k] = Rdelta.T.dot(delta) / Nk + np.eye(D)*smoothing # D x D

        costs[i] = np.log(weighted_pdfs.sum(axis = 1)).sum()
        print(costs[i])

        if i > 0:
            if np.abs(costs[i] - costs[i-1]) < 0.1:
                break

    plt.plot(costs)
    plt.title('Costs')
    plt.show()

    random_colors = np.random.random((K,3))
    colors = R.dot(random_colors)
    plt.scatter(X[:,0],X[:,1],c = colors)
    plt.title('Gaussian Mixture Model')
    plt.show()

    print(f'pi : {pi}')
    print(f'means : {M}')







def get_simple_data():
    ## D is the no. of dimensions
    D = 2
    ## s is distance by which various gaussian clouds are separated
    s = 4

    ### There are 3 differnet gaussian clouds with different means as given
    mu1 = np.array([0,0])
    mu2 = np.array([s,s])
    mu3 = np.array([0,s])

    N = 2000
    X = np.zeros((N,D))

    ## Filling the points with normal random variables
    X[:1200,:] = np.random.randn(1200,D)*2 + mu1
    X[1200:1800,:] = np.random.randn(600,D) + mu2
    X[1800:,:] = np.random.randn(200,D)*0.5 + mu3

    return X


def main():

    X = get_simple_data()
    plt.scatter(X[:,0],X[:,1])
    plt.show()

    gmm(X,K = 3)





if __name__ == '__main__':
    main()
