from shutil import which
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#DEFINITION
    #List of points coords
L = [(4,4), (3.5,7.5), (2.57, 5.59), (4, 6), (3.8, 2.7), 
    (0.5, 6), (3.5, 5), (3, 6), (2, 8), (1, 7), 
    (2, 6), (2, 2), (4.72, 4.46), (5, 6),
    (1.5, 5), (2, 3), (2,4), (3.3, 4.2), (1.23, 3.59),
    (2.5, 5), (3.5, 5.5), (3.01, 3.41)
    ]

    #String of ALL points names
pt_list = "ABCDEFGHIJKLMNQPRSTUVZ"

    #List of BLUE points names
pts_blue = "BCDFHIJKNQUV"
    #List of RED points names
pts_red = "AEGLMPRSTZ"


    #Coords for the RED points
X_red = np.array([i[0] for i in L if pt_list[L.index(i)] in pts_red])
Y_red = np.array([i[1] for i in L if pt_list[L.index(i)] in pts_red])

    #Coords for the BLUE points
X_blue = np.array([i[0] for i in L if pt_list[L.index(i)] in pts_blue])
Y_blue = np.array([i[1] for i in L if pt_list[L.index(i)] in pts_blue])


annotations_blue=[i for i in pts_blue]
annotations_red=[i for i in pts_red]


#Graph settings
    #GRID
plt.grid(linestyle='-', linewidth=1,alpha=0.7)
    #Graph LIMITS
ax = plt.gca()
#ax.set_xlim([-3, 9])
#ax.set_ylim([0, 9])
    #Axis names
plt.xlabel("X")
plt.ylabel("Y")
    #Graph title
plt.title("Graph KNN",fontsize=15)

#Place the points (RED, BLUE, o)
plt.scatter(X_red,Y_red,s=50,color="red", marker='x')
plt.scatter(X_blue,Y_blue,s=50,color="blue", marker='o')
plt.scatter(3,5,s=100,color='black', marker='+')

#Naming the points

    #RED
for i, label in enumerate(annotations_red):
    plt.annotate(label, (X_red[i]+0.05, Y_red[i]+0.05), color='red')

    #BLUE
for i, label in enumerate(annotations_blue):
    plt.annotate(label, (X_blue[i]+0.05, Y_blue[i]+0.05), color='blue')

    #O
plt.annotate('O', (3+0.05, 5+0.05))



plt.show()