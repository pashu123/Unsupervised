## This Repository Explains various Unsupervised Learning Techniques and their Disadvantages

# Uses of Unsupervised Learning

<ul>
<li> Density Estimation 
<li> Finding Latent Variables
<li> Dimensionality Reduction
</ul>

# K Means Clustering

### Algorithm

<b> Initialize: </b><i> Pick K Random Points to be the Cluster Centers. </i> <br>
<i> While not converged: <br>
Assign each points to the nearest cluster center. <br>
Recalculate each cluster center from points that belong to it. </i> <br>


<img src="https://latex.codecogs.com/gif.latex?\textit{Initialize&space;}&space;m_1\text{&space;}&space;...\text{&space;}&space;m_k&space;\text{&space;random&space;points&space;in&space;X}\\&space;\textit{While&space;not&space;converged}:&space;\\&space;Step1:&space;\text{Calculate&space;cluster&space;responsibilities&space;:}&space;r_k^n&space;=&space;\frac{exp&space;[-\beta&space;\text{&space;}&space;d(m_k,x^n)]}{&space;\sum_j&space;exp[-\beta\text{&space;}d(m_j,x^n)]}&space;\\&space;Step2:&space;\text{Recalculate&space;Means&space;:&space;}&space;m_k&space;=&space;\frac{\sum_n&space;r_k^nx^n}{\sum_n&space;r_k^n}" title="\textit{Initialize } m_1\text{ } ...\text{ } m_k \text{ random points in X}\\ \textit{While not converged}: \\ Step1: \text{Calculate cluster responsibilities :} r_k^n = \frac{exp [-\beta \text{ } d(m_k,x^n)]}{ \sum_j exp[-\beta\text{ }d(m_j,x^n)]} \\ Step2: \text{Recalculate Means : } m_k = \frac{\sum_n r_k^nx^n}{\sum_n r_k^n}" />

