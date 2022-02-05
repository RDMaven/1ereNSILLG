import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

global my_colors
my_colors=['g','r','b']

#+------------------------------------------------------+#

def charger_data():
    data=[]
    file=open("./Algo - KNN/iris.csv","r")
    file.readline() #extraire la première ligne
    iris=file.read().strip().split('\n')    #nettoyer et séparer les coordonnées des points
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

def afficher_point(pt,lab):
    
    if lab == 0:
        color_pts = 'green'
    elif lab == 1:
        color_pts = 'red'
    elif lab == 2:
        color_pts = 'blue'
    
    plt.scatter(pt[0],pt[1],s=50,marker='x', color=color_pts)

#+------------------------------------------------------+#

def distance(a,b):
    """d : distance entre deux points"""
    d = 0
    for i in range(len(a)):
        d = d + (b[i]-a[i])**2
    return sqrt(d)

#+------------------------------------------------------+#

def listdist(data, o):
    """
    L_dist : la list de distances des points.
    L_pts_dist : idem, mais sous forme de tuple avec la lettre associée.
    n : longueur de la liste L donnée.
    """
    pts_L = [tuple(map(int, i.split(','))) for i in data]
    pts_coords = [(i[0],i[1]) for i in pts_L]
    L_dist = []
    n = len(data)
    for i in range(n):
        L_dist.append( [(distance(o,(pts_L[i][0], pts_L[i][1]))),pts_L[i][2]] )
    return L_dist

#+------------------------------------------------------+#

def kppv(ld, k, o):
    """
    knn : liste des k points les plus proches.
    D : la liste des distances triée.
    """
    knn = []
    D = sorted(ld)
    for i in range(k):
        knn.append(D[i])

    return knn

#+------------------------------------------------------+#

def prediction(lk):
    g,r,b=0,0,0
    for i in lk:
        if i[1] == 0:
            g += 1
        if i[1] == 1:
            r += 1
        if i[1] == 2:
            b += 1
    couleur = max(r,g,b)
    if couleur == r:
        return 1
    elif couleur == b:
        return 2
    elif couleur == g:
        return 0

#+------------------------------------------------------+#
#+------------------------------------------------------+#

'''Programme principal'''
table = charger_data()
#print(len(table))
afficher(table)

point=(48,17)
ld=listdist(table,point)
k=3#len(table)
lk=kppv(ld,k,point)
ck=prediction(lk)
afficher_point(point,ck)

plt.show()
