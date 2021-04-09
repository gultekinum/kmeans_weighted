import numpy as np
import matplotlib.pyplot as plt
from random import randint

def random_data_generator():
    center_1 = np.array([1,1])
    center_2 = np.array([5,5])
    center_3 = np.array([8,1])

    data_1 = np.random.randn(200, 2) + center_1
    data_2 = np.random.randn(200,2) + center_2
    data_3 = np.random.randn(200,2) + center_3

    data = np.concatenate((data_1, data_2, data_3), axis = 0)

    plt.scatter(data[:,0], data[:,1], s=7)
    return data

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def add_weight(data):
    weighted_points = {}
    counter = 0
    for point in data:
        x,y,weight = point[0],point[1],randint(1,3)
        weighted_points[counter]=x,y,weight
        counter+=1
    return weighted_points

def regular_kmeans(data):
    #k means starting
    cent1 = np.random.randn(1,2)
    cent2 = np.random.randn(1,2)
    cent3 = np.random.randn(1,2)

    cluster_dict = {}

    cluster_dict[cent1[0][0],cent1[0][1]]=[]
    cluster_dict[cent2[0][0],cent2[0][1]]=[]
    cluster_dict[cent3[0][0],cent3[0][1]]=[]

    for j in range(20):
        for point in data:
            res = []
            for centers in cluster_dict:

                cx = centers[0]
                cy = centers[1]
                temp=[centers,distance(cx,cy,point[0],point[1])]
                res.append(temp)
            min_value = min(res, key = lambda t: t[1])
            temp = []
            temp.append(point[0])
            temp.append(point[1])
            cluster_dict[min_value[0]].append(temp)

        new_centers = []
        old_centers = []

        for center in cluster_dict:
            x_total = 0
            y_total = 0
            for point in cluster_dict[center]:
                x_total+=point[0]
                y_total+=point[1]
            mean_x = (x_total+center[0])/(len(cluster_dict[center])+1)
            mean_y = (y_total+center[1])/(len(cluster_dict[center])+1)

            temp = []
            temp.append(mean_x)
            temp.append(mean_y)
            new_centers.append(temp)

        for center in cluster_dict:
            old_centers.append(center)

        if j!=19:
            cluster_dict ={}
            for center in new_centers:
                cluster_dict[center[0],center[1]] = [] 
    return cluster_dict

def weighted_kmeans(weighted_points):
    #k means starting
    cent1 = np.random.randn(1,2)
    cent2 = np.random.randn(1,2)
    cent3 = np.random.randn(1,2)

    cluster_dict = {}

    cluster_dict[cent1[0][0],cent1[0][1]]=[]
    cluster_dict[cent2[0][0],cent2[0][1]]=[]
    cluster_dict[cent3[0][0],cent3[0][1]]=[]

    for j in range(20):
        for point in weighted_points:
            res = []
            for centers in cluster_dict:

                cx = centers[0]
                cy = centers[1]
                temp=[centers,distance(cx,cy,weighted_points[point][0],weighted_points[point][1])]
                res.append(temp)
            min_value = min(res, key = lambda t: t[1])
            temp = []
            temp.append(weighted_points[point][0])
            temp.append(weighted_points[point][1])
            temp.append(weighted_points[point][2])
            cluster_dict[min_value[0]].append(temp)

        new_centers = []
        old_centers = []

        for center in cluster_dict:
            x_total = 0
            y_total = 0
            element_number = 0
            for point in cluster_dict[center]:
                x_total+=point[0]*point[2]
                y_total+=point[1]*point[2]
                element_number +=point[2]
                
            mean_x = (x_total+center[0])/(element_number+1)
            mean_y = (y_total+center[1])/(element_number+1)

            temp = []
            temp.append(mean_x)
            temp.append(mean_y)
            new_centers.append(temp)

        for center in cluster_dict:
            old_centers.append(center)

        if j!=19:
            cluster_dict ={}
            for center in new_centers:
                cluster_dict[center[0],center[1]] = [] 
    return cluster_dict

def plot_clusters(min_x, min_y, max_x, max_y, cluster_dict):

    plot_size = 3.5
    plt.xlim(min_x*plot_size, max_x*plot_size)
    plt.ylim(min_y*plot_size, max_y*plot_size)

    color = []
    
    for center in cluster_dict:
        name = "cluster "+str(center)
        color.append(name)
    
    
    counter = 0
    for center in cluster_dict:
        x_arr = []
        y_arr = []
        for point in cluster_dict[center]:
            x_arr.append(point[0])
            y_arr.append(point[1])
        plt.scatter(x_arr, y_arr, s=4, label=color[counter])
        counter+=1


data = random_data_generator()
cluster_dict = regular_kmeans(data)
for center in cluster_dict:
    min_value_x = min(cluster_dict[center], key = lambda t: t[0])[0]
    max_value_x = max(cluster_dict[center], key = lambda t: t[0])[0]
    min_value_y = min(cluster_dict[center], key = lambda t: t[1])[1]
    max_value_y = max(cluster_dict[center], key = lambda t: t[1])[1]
    
plot_clusters(min_value_x, min_value_y, max_value_x, max_value_y,cluster_dict)
    
weighted_dict = add_weight(data)
weighted_dict= weighted_kmeans(weighted_dict)
for center in weighted_dict:
    min_value_x = min(weighted_dict[center], key = lambda t: t[0])[0]
    max_value_x = max(weighted_dict[center], key = lambda t: t[0])[0]
    min_value_y = min(weighted_dict[center], key = lambda t: t[1])[1]
    max_value_y = max(weighted_dict[center], key = lambda t: t[1])[1]
    
plot_clusters(min_value_x, min_value_y, max_value_x, max_value_y,weighted_dict)