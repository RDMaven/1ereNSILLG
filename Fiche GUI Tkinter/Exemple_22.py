from tkinter import *
fenetre = Tk()
# label
label = Label(fenetre, text="Hello !",fg="red",bg="black")
label.place(x=10, y=90)
# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)
bouton.pack()
# input
value = StringVar()
value.set("texte par defaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()
# checkbutton
bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()
# radiobutton
val = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=val, val=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=val, val=2)
bouton3 = Radiobutton(fenetre, text="Peut-être", variable=val, val=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "Arduino")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
liste.pack()
# canvas
canvas = Canvas(fenetre, width=150, height=120, background='blue')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="red")
canvas.pack()
# scrollbar
valuesc = DoubleVar()
scale = Scale(fenetre, variable=valuesc)
scale.pack()
# spinbox
s = Spinbox(fenetre, from_=0, to=10)
s.pack()
#Pour récupérer la valeur d'un input il vous faudra utiliser la méthode
#cget() pour un bouton ou get() pour une entrée texte

def recupere():
    if boutonv.cget('text')=='Valider':
        boutonv['text']='ok' # ou boutonv.config(text = 'ok')
    else :
        boutonv.config(text = 'Valider')
boutonv = Button(fenetre, text="Valider", command=recupere)
boutonv.pack()
fenetre.mainloop()