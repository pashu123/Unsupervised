import numpy as np
import matplotlib.pyplot as plt


def d(u,v):
    diff = u-v
    return diff.dot(diff)


def cost(X,R,M):
    cost = 0
    for k in range(len(M)):
        for n in range(len(X)):
            cost += R[n,k] * d(M[k],X[n])

    return cost


def plot_k_means(X,K,max_iter = 20,beta = 1.0):

    N,D = X.shape
    M = np.zeros((K,D))
    R = np.zeros((N,K))

    for k in range(K):
        M[k] = X[np.random.choice(N)]

    
    grid_width = 5
    grid_height = (max_iter / grid_width) * 1.2
    random_colors = np.random.random((K,3))
    plt.figure()

    costs = np.zeros(max_iter)

    for i in range(max_iter):
        colors = R.dot(random_colors)
        plt.subplot(grid_width,grid_height,i+1)
        plt.scatter(X[:,0],X[:,1],c = colors)

        for k in range(K):
            for n in range(N):
                R[n,k] = np.exp(-beta * d(M[k],X[n]))/ np.sum(np.exp(-beta * d(M[j],X[n])) for j in range(K))

        for k in range(K):
            M[k] = R[:,k].dot(X) / R[:,k].sum()
        

        costs[i] = cost(X,R,M)

        if i > 0:
            if np.abs(costs[i] - costs[i-1]) < 0.1:
                break

    
    plt.show()
    # plt.plot(costs)
    # plt.title("costs")
    # plt.xlabel('No. of iterations')
    # plt.ylabel('Average Mean Distance')
    # plt.show()

    # random_colors = np.random.random((K,3))
    # colors = R.dot(random_colors)

    # plt.scatter(X[:,0],X[:,1],c = colors)
    # plt.show() 

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

    ## Sanity check
    plt.scatter(X[:,0],X[:,1])
    plt.show()


    K = 3
    plot_k_means(X,K)

    K = 5
    plot_k_means(X,K)

    K = 5
    plot_k_means(X,K,max_iter = 30,beta = 0.3)

if __name__ == '__main__':
    main()