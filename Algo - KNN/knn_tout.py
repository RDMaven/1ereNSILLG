# Un algorithme permettant de déterminer les k plus proches voisins de O 
# en prenant les points indiqués dans le graph (cf fiche...)
# + graph

#+----------------- IMPORTS -----------------+#
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
#+-------------------------------------------+#

#+----------------- GRAPH SETTINGS -----------------+#
plt.title("Graph KNN",fontsize=15)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(linestyle='-', linewidth=1,alpha=0.7)
#Optional : Graph LIMITS
#ax = plt.gca()
#ax.set_xlim([-3, 9])
#ax.set_ylim([0, 9])
#+--------------------------------------------------+#


#+------------------------ FUNCTIONS ------------------------+#

    #1 : distance(), distance Euclidienne entre deux points

def distance(a,b):
    """d : distance entre deux points"""
    d = 0
    for i in range(len(a)):
        d = d + (b[i]-a[i])**2
    return sqrt(d)

    #2 : listdist(), liste de distances

def listdist(L, o):
    """
    L_dist : la list de distances des points.
    L_pts_dist : idem, mais sous forme de tuple avec la lettre associée.
    n : longueur de la liste L donnée.
    """
    L_dist = []
    L_pts_dist = []
    n = len(L)
    for i in range(n):
        L_dist.append( distance(o, L[i]) )
        L_pts_dist.append( (distance(o,L[i]),L_pts[i]) )
    return L_dist, L_pts_dist

    #3 : kppv(), les knn

def kppv(L, k, o):
    """
    knn : liste des k points les plus proches.
    D : la liste des distances triée.
    D_l : idem avec la liste associant distance et lettre.
    """
    knn = []
    D = sorted(listdist(L,o)[0])
    D_l = listdist(L,o)[1]
    D_l.sort(key=lambda y: y[0])
    for i in range(k-1):
        knn.append(D[i])
    return knn, D_l[:k-1]

#+-----------------------------------------------------------+#


#+----------------- DEFINITION - Points -----------------+#
#Coords
L = [(4,4), (3.5,7.5), (2.57, 5.59), (4, 6), (3.8, 2.7), (0.5, 6), (3.5, 5), (3, 6), (2, 8), (1, 7), (2, 6), (2, 2), (4.72, 4.46), (5, 6), (1.5, 5), (2, 3), (2,4), (3.3, 4.2), (1.23, 3.59), (2.5, 5), (3.5, 5.5), (3.01, 3.41)]

#Names
pt_list = "ABCDEFGHIJKLMNQPRSTUVZ"
L_pts = [l for l in "ABCDEFGHIJKLMNQPRSTUVZ"]
#+-------------------------------------------------------+#


#+----------------- BLUE POINTS -----------------+#

#List of BLUE points names
pts_blue = "BCDFHIJKNQUV"

#Coords of points
X_blue = np.array([i[0] for i in L if pt_list[L.index(i)] in pts_blue])
Y_blue = np.array([i[1] for i in L if pt_list[L.index(i)] in pts_blue])

#Name of points
annotations_blue=[i for i in pts_blue]

#Place points
plt.scatter(X_blue,Y_blue,s=50,color="blue", marker='o')

#Annotate points
for i, label in enumerate(annotations_blue):
    plt.annotate(label, (X_blue[i]+0.05, Y_blue[i]+0.05), color='blue')

#+-----------------------------------------------+#


#+----------------- RED POINTS -----------------+#

#List of RED points names
pts_red = "AEGLMPRSTZ"

#Coords of points
X_red = np.array([i[0] for i in L if pt_list[L.index(i)] in pts_red])
Y_red = np.array([i[1] for i in L if pt_list[L.index(i)] in pts_red])

#Name of points
annotations_red=[i for i in pts_red]

#Place points
plt.scatter(X_red,Y_red,s=50,color="red", marker='x')

#Annotate points
for i, label in enumerate(annotations_red):
    plt.annotate(label, (X_red[i]+0.05, Y_red[i]+0.05), color='red')

#+----------------------------------------------+#


#+----------------- O POINT -----------------+#
try:X_o = float(input("Abscisse du point O : "))
except: print("Bad input.")
try:Y_o = float(input(" Ordonné du point O : "))
except: print("Bad input.")
o = (X_o,Y_o)

#Place point
plt.scatter(X_o,Y_o,s=100,color='black', marker='+')

#Annotate points
plt.annotate('O', (X_o+0.05, Y_o+0.05))

#+-------------------------------------------+#


#+------------------------ Calcul des KNN ------------------------+#
k = int(input("Nombre de 'plus proches voisins' : "))

knn = kppv(L,10,o)

#Liste des distances.
print()
print(knn[0])

#Liste des points
pts = [i[1] for i in knn[1]]
print(*pts)

#Couleur de O.

couleur = 0
for i in pts:
    if i in pts_blue:
        couleur+=1
    if i in pts_red:
        couleur-=1

if couleur > 0:
    print(f"{couleur} : O est bleu.")
elif couleur < 0:
    print(f"{couleur} : O est rouge.")
elif couleur == 0:
    print(f"{couleur} : tu choisis.")

#+----------------------------------------------------------------+#




plt.show()