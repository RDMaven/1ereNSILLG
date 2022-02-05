import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

#+------------------------------------------------------+#

def charger_data():
    data=[]
    file=open("./Algo - KNN/pokemon.csv","r")
    file.readline()
    iris=file.read().strip().split('\n')
    data = iris
    file.close()
    return data

#+------------------------------------------------------+#

def afficher(data): 
    plt.title("Classification des trois variétés d'iris")
    plt.xlabel("Longueur de la pétale (en mm)")
    plt.ylabel("Largeur de la pétale (en mm)")
    plt.grid(which = "both", linestyle = "--")
       
    pts_L = [tuple(map(int, i.split(','))) for i in data]
    
    pts_X = np.array([i[0] for i in pts_L])
    pts_Y = np.array([i[1] for i in pts_L])
    
    pts_g_x = []
    pts_g_y = []
    pts_r_x = []
    pts_r_y = []
    pts_b_x = []
    pts_b_y = []
    
    for i in pts_L :
        if i[2] == 0:
            color_pts = 'green'
            pts_g_x.append(i[0])
            pts_g_y.append(i[1])
            plt.scatter(pts_g_x,pts_g_y,s=50,color=color_pts)
            
        elif i[2] == 1:
            color_pts = 'red'
            pts_r_x.append(i[0])
            pts_r_y.append(i[1])
            plt.scatter(pts_r_x,pts_r_y,s=50,color=color_pts)
        elif i[2] == 2:
            color_pts = 'blue'
            pts_b_x.append(i[0])
            pts_b_y.append(i[1])
            plt.scatter(pts_b_x,pts_b_y,s=50,color=color_pts)
        
#+------------------------------------------------------+#

print(charger_data())
