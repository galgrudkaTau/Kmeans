import sys 
import math 

""" TODO:  update centroids
write to the outputfile 
take care of continue condition 
check validity of input
 """

def file_to_matrix(input_file):
    input_mat = []

    f = open(input_file, "r")
    for line in f:
        currentline = line.split(",")
        last = currentline[-1][:-1]
        currentline = currentline[:-1]
        currentline.append(last)
        currentline = [float(i) for i in currentline]
        input_mat.append(currentline)
    #input_mat.pop()
    f.close() 
    return input_mat   
    #print(input_mat)

def create_centroids(k, input_mat):
    centroids=[]
    centroids[i]=[input_mat[i] for i in range(k)]

def calculate_distance(centroid, data_point):
    return sum([pow(centroids[i]-datapoint[i],2) for i in range(len(centroid))])

def calculate_norma(centroid, data_point):
    return math.sqrt([pow(centroids[i]-datapoint[i],2) for i in range(len(centroid))])

def assign_to_clusters(input_mat,centroids,k):
    clusters=[None]*k
    """  
        1) for each item in the input list
            2) for each centroid
                3) calculate distance 
                4) update minimum distance and cluster _i_ from which the distance is minimal
            5) add item to the list in cluster _i_
           """
    #infinity = float("inf")
    #sys.float_info.max

    for idx,data_point in enumerate(input_mat):
        distance= float("inf")
        temp_dist=0
        cluster_index=0
        for i, centroid in enumerate(centroids):
            temp_dist=calculate_distance(centroid, data_point)
            if (temp_dist<distance):
                distance=temp_dist
                cluster_index=i
        if (clusters[cluster_index] == None):
            clusters[cluster_index]=[idx]
        else: 
            clusters[cluster_index].append(idx)
    return clusters


def update_centroids(input_mat,centroids,clusters):

def kmeans(max_iter=200):
    iter=0
    continue=True
    while(iter<max_iter and continue):
        """
        1) for each item in the input list
            2) for each centroid
                3) calculate distance 
                4) update minimum distance and cluster _i_ from which the distance is minimal
            5) add item to the list in cluster _i_

        6) update centroids 
        7) update iter
        8) update continue_codition """
        
        clusters=assign_to_clusters(input_mat,centroids)
        update_centroids(input_mat,centroids,clusters)
        iter+=1

def main(): 
    input_file=None
    output_file=None
    k=int(sys.argv[1])
    #take care of type cheching- is it int? 
    if(len(sys.argv)==4):
        input_file=sys.argv[2]
        output_file=sys.argv[3]
        
    if (len(sys.argv)==5):
        max_iter=int(sys.argv[2])
        input_file=sys.argv[3]
        output_file=sys.argv[4]
    
    #Reading from file
    data_point_matrix=file_to_matrix(input_file)
    create_centroids(k, input_mat)
    





       



main()