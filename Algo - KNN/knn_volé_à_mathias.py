from tkinter import *
from math import sqrt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fenetre = Tk()


# --------------- Configuration de la fenêtre ---------------
fenetre.overrideredirect(False)
fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))

# --------------- Récupération des coordonnées souhaitées ---------------
def reset():
    global value_x, value_y, value_k, entree_x, entree_y, entree_k, boutonv, bg, label1

    for widget in fenetre.winfo_children():
        widget.destroy()

    fenetre.configure(bg='#5CC7B2')
    fenetre.columnconfigure(0, minsize=(fenetre.winfo_screenwidth()/10)) 
    fenetre.columnconfigure(1, minsize=(fenetre.winfo_screenwidth()*9/10))  

        #Définition de la box input_x
    value_x = StringVar()
    value_x.set("Coordonnée en x")
    entree_x = Entry(fenetre, textvariable=value_x, width=30)
    entree_x.grid(row=0,column=0, padx=20, pady=20)

        #Définition de la box input_y
    value_y = StringVar()
    value_y.set("Coordonnée en y")
    entree_y = Entry(fenetre, textvariable=value_y, width=30)
    entree_y.grid(row=1,column=0, padx=20, pady=20)

        #Définition de la box k: Combien de voisins?
    value_k = StringVar()
    value_k.set("Combien de voisins doivent être pris en compte pour déterminer la couleur du point ?")
    entree_k = Entry(fenetre, textvariable=value_k, width=30)
    entree_k.grid(row=2,column=0, padx=20, pady=20)

        #Définition du bouton valider
            #Définition de la fonction qui récupère les coordonnées au click sur le bouton
    def recupere():
        global o, k, a, b
        if boutonv.cget('text')=='Valider':
            try:
                a = float(entree_x.get())
                b = float(entree_y.get())
                k = int(entree_k.get())
                o = (a,b)

                reset()
                mainProgramme()
            except:
                reset()
                Label(fenetre,text='Veuillez entrer un nombre valide. Pour rappel, les chiffres décimaux s\'écrivent avec un point ".", vous pouvez réessayer.').grid(row=0, column=1)

        else :
            boutonv.config(text = 'Valider')

    boutonv = Button(fenetre, text="Valider", command=recupere)
    boutonv.grid(row=3,column=0, padx=20, pady=20)

reset()

# --------------- K PLUS PROCHES VOISINS ---------------
    #Déclaration de toutes les variables nécessaires
global L, listeLettre, a, b, k, o, color
L=[(4,4),(3.5,7.5),(2.57,5.59),(4,6),(3.8,2.7),(0.5,6),(3.5,5),(3,6),(2,8),(1,7),(2,6),(2,2),(4.72,4.46),(5,6),(1.5,5),(2,3),(2,4),(3.3,4.2),(1.23,3.59),(2.5,5),(3.5,5.5),(3.01,3.41)]
color=['red','blue','blue','blue','red','blue','red','blue','blue','blue','blue','red','red','blue','blue','red','red','red','red','blue','blue','red']
listeLettre=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Q','P','R','S','T','U','V','Z',]

    #Définition de la fonction traçant les graphiques
def graphique(voisins,étape) : 
    fig = Figure(figsize=(6, 4), dpi=96)
    ax = fig.add_subplot(111)

    x=[]
    y=[] 
    for g in range(len(L)) : #création de la liste des coordonnées en x
        x.append(L[g][0])
    for h in range(len(L)) : #création de la liste des coordonnées en y
        y.append(L[h][1])

    
    ax.axis('equal')  #configuration des axes
    ax.grid(alpha=0.25)  #configuration de la grille du graphique
    
    for t in range(len(L)) :   #mise en place des noms de chaque point
        ax.text(L[t][0]-0.45, L[t][1], s=listeLettre[t], c=color[t])
    ax.scatter(x, y, c=color, alpha=1, label=listeLettre) #on trace le nuage de point
    
    if étape==1 : #on vérifie à quelle étape on se trouve
        ax.scatter(a,b, marker='X',c='black', s=100) #on place le point choisi   
        #pyplot.text(a-0.45, b, s='O', c='black')  -> mise en place du nom du point choisi (j'ai préféré l'enlever mais on peut le mettre si on le souhaite)

    graph = FigureCanvasTkAgg(fig, master=fenetre)
    canvas = graph.get_tk_widget()
    canvas.grid(row = u+3, pady=2, column=1)


    #Déterminations des plus proches voisins
def distance(a,b) :
    d=0
    d+=((b[0]-a[0])**2+(b[1]-a[1])**2)
    return round(sqrt(d),2)

def listdist(L,o) :
    n=len(L)
    listeDist={}
    for i in range(n) :
        listeDist[listeLettre[i]]=distance(L[i],o)
    return listeDist

def kppv(L,o,k) :
    D=sorted(listdist(L,o).items(),key=lambda a: a[1])
    knn=[]
    for i in range(k):
        knn.append(D[i])
    return knn


    #Calcul des distances et tracé des graphiques
def mainProgramme() :
    global u
    knn=kppv(L,o,k)
    Label(fenetre,text="\nLes " + str(k) + " plus proches voisins du point choisi sont (point, distance par rapport au point choisi, couleur) :").grid(row=0,pady=2, column=1)
    couleurP=0
    couleur=0
    for u in range(k) : #cette boucle permet de compter le nombre de fois où la couleur 'red' appara^t afin de déterminer la couleur du point
        Label(fenetre,text=(knn[u][0] + '\t' + str(knn[u][1]) + "\t" + color[listeLettre.index(knn[u][0])])).grid(row=u+1, column=1)
        if color[listeLettre.index(knn[u][0])]=='red' :
            couleurP+=1
        if couleurP>(k/2) :
            couleur='Le point sera donc de couleur rouge.'
            couleur_en = "red"
        elif couleurP==(k/2) :
            couleur='La couleur du point est indéterminée.'
            couleur_en = "grey"
        else :
            couleur='Le point sera donc de couleur bleu.'
            couleur_en = "blue"
    Label(fenetre,text=couleur, bg=couleur_en).grid(row=u+2, pady=2, column=1)

    graphique(knn, 1)

fenetre.mainloop()

