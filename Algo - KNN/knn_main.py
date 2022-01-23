# Un algorithme permettant de déterminer les k plus proches voisins de O 
# en prenant les points indiqués dans le graph (cf fiche...)

#+----------------- IMPORTS -----------------+#
from math import sqrt
#+-------------------------------------------+#


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


#+------------------------ Les valeurs données ------------------------+#

#liste des points :
l = [(4,4), (3.5,7.5), (2.57, 5.59), (4, 6), (3.8, 2.7), 
    (0.5, 6), (3.5, 5), (3, 6), (2, 8), (1, 7), 
    (2, 6), (2, 2), (4.72, 4.46), (5, 6),
    (1.5, 5), (2, 3), (2,4), (3.3, 4.2), (1.23, 3.59),
    (2.5, 5), (3.5, 5.5), (3.01, 3.41)
    ]

#liste des points dans l'ordre d'apparition dans la liste L.
L_pts = [l for l in "ABCDEFGHIJKLMNQPRSTUVZ"]

#BLUE and RED points
pts_blue = "BCDFHIJKNQUV"
pts_red = "AEGLMPRSTZ"
#+---------------------------------------------------------------------+#

#+------------------------ O ------------------------+#
try:X_o = float(input("Abscisse du point O : "))
except: print("Bad input.")
try:Y_o = float(input(" Ordonné du point O : "))
except: print("Bad input.")
o = (X_o,Y_o)
#+---------------------------------------------------+#

#+------------------------ Calcul des KNN ------------------------+#
k = int(input("Nombre de 'plus proches voisins' : "))

knn = kppv(l,10,o)

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
