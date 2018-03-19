# K-Means
K-Means classification algorithm implemented in Python to cluster the unclustered dataset based on certain criteria. The criteria includes:

1) User specified number of clusters for K-Means algorithm

2) The maximum number of iterations for the algorithm

3) The epsilon value (change of the sum of the distance from the centroids between iterations)

## Instruction
To Run the program use the following command: 

**python kMeans.py <filename> <Number of Clusters> <Iterations> <Epsilon>**

where,

	filename = the name of the .arff dataset
	Number of clusters = the value of k,
	iterations = the maximum number of iterations
	Epsilon = the minimum threshold for changes in sse

Example: 
	python kMeans.py wineN.arff 4 100 0
	
After running the code, the output will generated in the same directory as k.output.txt, where k is the number of cluster number 

