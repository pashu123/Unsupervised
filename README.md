## This Repository Explains various Unsupervised Learning Techniques and their Disadvantages

# Uses of Unsupervised Learning

<ul>
<li> Density Estimation 
<li> Finding Latent Variables
<li> Dimensionality Reduction
</ul>

# K Means Clustering

### Algorithm:

Initialize: <i> Pick K Random Points to be the Cluster Centers. </i><br> <br>
<i> While not converged: <br>
Assign each points to the nearest cluster center. <br>
Recalculate each cluster center from points that belong to it. </i> <br>

# Soft K Means Clustering

### Algorithm

<img src="https://latex.codecogs.com/gif.latex?\textit{Initialize&space;}&space;m_1\text{&space;}&space;...\text{&space;}&space;m_k&space;\text{&space;random&space;points&space;in&space;X}\\&space;\textit{While&space;not&space;converged}:&space;\\&space;Step1:&space;\text{Calculate&space;cluster&space;responsibilities&space;:}&space;r_k^n&space;=&space;\frac{exp&space;[-\beta&space;\text{&space;}&space;d(m_k,x^n)]}{&space;\sum_j&space;exp[-\beta\text{&space;}d(m_j,x^n)]}&space;\\&space;Step2:&space;\text{Recalculate&space;Means&space;:&space;}&space;m_k&space;=&space;\frac{\sum_n&space;r_k^nx^n}{\sum_n&space;r_k^n}" title="\textit{Initialize } m_1\text{ } ...\text{ } m_k \text{ random points in X}\\ \textit{While not converged}: \\ Step1: \text{Calculate cluster responsibilities :} r_k^n = \frac{exp [-\beta \text{ } d(m_k,x^n)]}{ \sum_j exp[-\beta\text{ }d(m_j,x^n)]} \\ Step2: \text{Recalculate Means : } m_k = \frac{\sum_n r_k^nx^n}{\sum_n r_k^n}" />


## Visualization of Convergence of Soft Kmeans

![cluster_1](https://user-images.githubusercontent.com/16246821/75245208-4553a300-57f3-11ea-98b8-26bdd1190d6a.png)


## K_Means Fails on These Distribution

### Donut

![fail1](https://user-images.githubusercontent.com/16246821/75246836-9add7f00-57f6-11ea-9f10-abab77da5cad.png)

### Multivariate Gaussian

![fail2](https://user-images.githubusercontent.com/16246821/75246842-9ca74280-57f6-11ea-8861-6756786946f9.png)

### Gaussian with different Density

![fail3](https://user-images.githubusercontent.com/16246821/75246832-987b2500-57f6-11ea-9df1-4de0241f6653.png)


## Disadvantages of K Means

<ol>
<li> You have to choose K 
<li> Stuck in Local Minima 
<li> Sensitive to Initial Configuration
<li> Can't Solve the Donut Problem
<li> Doesn't Take into account Density of the cluster

</ol>


# Hierarchial Clustering

### Ward Linkage
![wardlinkage](https://user-images.githubusercontent.com/16246821/75453778-6c000e00-599a-11ea-87d7-9f2b0e1004db.png)

### Complete Linkage
![completelink](https://user-images.githubusercontent.com/16246821/75453754-63a7d300-599a-11ea-8df8-b18a92c57792.png)

### Single Linkage
![singlelinkage](https://user-images.githubusercontent.com/16246821/75453757-64d90000-599a-11ea-8342-fdf0977908bb.png)
