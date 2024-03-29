#+----------------- IMPORTS -----------------+#
import numpy as np
import matplotlib.pyplot as plt
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


#+----------------- DEFINITION - Points -----------------+#
#Coords
L = [(4,4), (3.5,7.5), (2.57, 5.59), (4, 6), (3.8, 2.7), (0.5, 6), (3.5, 5), (3, 6), (2, 8), (1, 7), (2, 6), (2, 2), (4.72, 4.46), (5, 6), (1.5, 5), (2, 3), (2,4), (3.3, 4.2), (1.23, 3.59), (2.5, 5), (3.5, 5.5), (3.01, 3.41)]

#Names
pt_list = "ABCDEFGHIJKLMNQPRSTUVZ"
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

#Coords of point
X_o = 3
Y_o = 5

#Place point
plt.scatter(X_o,Y_o,s=100,color='black', marker='+')

#Annotate points
plt.annotate('O', (X_o+0.05, Y_o+0.05))

#+-------------------------------------------+#


plt.show()