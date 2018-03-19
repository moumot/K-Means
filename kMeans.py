# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:14:05 2018

@author: chunqian
"""
import sys
import random
import math

import time
test = []
start_time = time.time()
 
datafile = str(sys.argv[1])
data = open(datafile)

rows = 0

for line in data:  #reading line from dataset to a list
    if(line[0] != '@' and line[0] != '\n'):   #check if it's a new line or attrobute
        test.append([])
        test[rows] = line.split(",")
        rows = rows+1

for i in range(rows):  #removing all '\n' symbol at the end of the rows
    test[i][len(test[i])-1] = test[i][len(test[i])-1][:-1]   

for i in range(rows):  #converting all string value to float list
    test[i] = list(map(float, test[i]))
    


columns = (len(test[0]))    

def main():
    k = int(sys.argv[2])
    iterate = int(sys.argv[3])
    epsilon = float(sys.argv[4])
    counter = 0
        
    centroids=[]
    centroidsNum=[]
    cluster=[]
    clusterNum = 0
    sse = 0
    nsse = 0
    
    centroidsNum = random.sample(range(0, len(test)), k)  #randomly picking k variables from the dataset
    output=open('./' + str(k) + '.output.txt', 'w+')
    output.write('<FIlename = ' + str(datafile) + ' k = ' + str(k) +', Maximum Iterations = ' + str(iterate) + ', Epsilon = ' + str(epsilon) + '>\n')
    output.write("\nInitial Centroid: " + "\n")
    for i in range(k):     #Initialzing empty centroids and clusters and assigning centroids based on index
        centroids.append([])
        cluster.append([])
        centroids[i] = test[centroidsNum[i]]
        output.write(str(i) + ": " + str(centroids[i]) + "\n")
        
    #centroids[0] = [13.3,1.72,2.14,17,94,2.4,2.19,0.27,1.35,3.95,1.02,2.77,1285]
    #centroids[1] = [12.22,1.29,1.94,19,92,2.36,2.04,0.39,2.08,2.7,0.86,3.02,312]
    #centroids[2] = [11.61,1.35,2.7,20,94,2.74,2.92,0.29,2.49,2.65,0.96,3.26,680]
    #First Iteration
    for i in range(0, len(test)):         #calculating sum of distance from centroids and assigning clusters to the centroids
        clusterNum = Cdistance(centroids, i)
        cluster[clusterNum].append(i) 
    
    for i in range(0,len(centroids)):    #calculating new centroids based on the average of the clusters
        centroids[i] = Cmean(cluster[i])
            
    sse = Csse(centroids,cluster)   #calculating sum of squared error 

    #Other Iterations
    while(counter < iterate-1 and (sse - nsse) > epsilon):  
        cluster = []
        for i in range(k):
            cluster.append([])
            
        for i in range(0, len(test)): #calculating sum of distance from centroids and assigning clusters to the centroids
            clusterNum = Cdistance(centroids, i)
            cluster[clusterNum].append(i)  
            
        if(counter != 0 ):
            sse = nsse      
            
        for i in range(0,len(centroids)): #calculating new centroids based on the average of the clusters
            centroids[i] = Cmean(cluster[i])
            
        nsse = Csse(centroids, cluster) #calculating sum of squared error 
        
        counter= counter + 1

    #output to file
    output.write("\nNumber of Iteration: " + str(counter+1) + '\n')    
    output.write("\nNew Centroids: " + "\n")
    for i in range(k):
        output.write(str(i) + ": " + str(centroids[i]) + "\n\n")
    
    output.write("\nCluster Instances: " + "\n")
    for i in range(k):
        percentage = len(cluster[i])*100/(len(test))
        output.write(str(i) + ": " + str(len(cluster[i])) + "(" + str(percentage) + "%)" + "\n")
        
    output.write("\nSquare Error: " + str(nsse))
    
    etime = time.time() - start_time
    output.write("\nExecution time: " + str(etime) + "\n\n\n")
    output.close()
    
    
def Cdistance(centroids,value):   #calculating sum of distance from centroids using euclidean distance method
    Dmin = float('inf')  #set minimum to infinity for comparing purpose 
    index = 0
    ssd = 0
    attributeSet = []
    attributeSet = test[value]  #change index number to the row values
    
    for i in range(len(centroids)):  #for every centroids
        ssd = 0
        for j in range(len(attributeSet)): #loop accross the attribute 
            ssd =  ssd + math.pow((attributeSet[j] - centroids[i][j]), 2)
            
        if(Dmin > ssd):
            Dmin = ssd
            index = i
            
    return  index

def Cmean(cluster):  #calculating the mean for the new centroids
    sumV = float(0)
    meanA = []
    for j in range(columns):   #for every attributes in the dataset
        sumV= 0
        for i in cluster:   #calculating sum of all value within a centroid's clusters
            sumV = sumV + test[i][j]
        meanA.append(float(sumV / len(cluster)))
        
    return meanA

def Csse(centroid, cluster):  #calculating the sum of error
    sseA = 0
    
    for i in range(len(centroid)):  #for every centroid
        for j in cluster[i]:  #for every cluster in a specific centroid
            for k in range(columns):  #calculate the sse across all columns
                sseA = sseA + math.pow((test[j][k]  - centroid[i][k]), 2)

    return sseA

def normalize(test):
    maxT = []
    minT = []
        
    for i in range(columns):
        maxT.append(max(l[i] for l in test))
        minT.append(min(l[i] for l in test))
    
    for i in range(rows):
        for j in range(columns):
            test[i][j] = (test[i][j] - minT[j])/(maxT[j] - minT[j])
    
    return test
    
    

test = normalize(test)
main()
