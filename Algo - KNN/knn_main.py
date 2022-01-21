# Un algorithme permettant de déterminer les k plus proches voisins de O 
# en prenant les points indiqués dans le graph (cf fiche...)

#=====================================================================================#
#===================================== Fonctions =====================================#
#=====================================================================================#

    #1. Fonction distance(): distance Euclidienne entre deux points

from math import sqrt
def distance(a,b):
    """d : distance entre deux points"""
    d = 0
    for i in range(len(a)):
        #def de la distance Euclidienne
        d = d + (b[i]-a[i])**2
    return sqrt(d)


    #2. Fonction listdist(): Liste de distances

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


    #3. Fonction kppv() : KNN...

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

#=====================================================================================#
#================================ KNN valeurs données ================================#
#=====================================================================================#

#La liste des points :
# A = (4, 4) # B = (3.5, 7.5) # C = (2.57, 5.59) # D = (4, 6) # E = (3.8, 2.7) 
# F = (0.5, 6) # G = (3.5, 5) # H = (3, 6) # I = (2, 8) # J = (1, 7) 
# K = (2, 6) # L = (2, 2) # M = (4.72, 4.46) # N = (5, 6) # O = (3,5)
# Q = (1.5, 5) # P = (2, 3) # R = (2,4) # S = (3.3, 4.2) # T = (1.23, 3.59) 
# U = (2.5, 5) # V = (3.5, 5.5) # Z = (3.01, 3.41)

L = [(4,4), (3.5,7.5), (2.57, 5.59), (4, 6), (3.8, 2.7), 
    (0.5, 6), (3.5, 5), (3, 6), (2, 8), (1, 7), 
    (2, 6), (2, 2), (4.72, 4.46), (5, 6),
    (1.5, 5), (2, 3), (2,4), (3.3, 4.2), (1.23, 3.59),
    (2.5, 5), (3.5, 5.5), (3.01, 3.41)
    ]

o = (3,5)

#Liste des points dans l'ordre d'apparition dans la liste L.
L_pts = [l for l in "ABCDEFGHIJKLMNQPRSTUVZ"]
pts_blue = "BCDFHIJKNQUV"
pts_red = "AEGLMPRSTZ"

#On calcule les 10 nn.
knn = kppv(L,10,o)
print(knn[0])

#On utilise la 2e liste retournée pour obtenir les points !
pts = [i[1] for i in knn[1]]
print(pts)

couleur = 0
for i in pts:
    if i in pts_blue:
        couleur+=1
    if i in pts_red:
        couleur-=1

if couleur > 0:
    print(f"{couleur} : O est bleu")
elif couleur < 0:
    print(f"{couleur} : O est rouge")
elif couleur == 0:
    print(f"{couleur} : tu choisis.")