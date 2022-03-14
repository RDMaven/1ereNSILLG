
from tkinter import *
from turtle import heading, right

fenetre = Tk()
fenetre.title("Animation")
Fond = Canvas(fenetre, width=600, height=600, bg="white")
Fond.pack()
btnQ = Button(fenetre, text='Quitter', command=fenetre.destroy)
btnQ.pack()


images= []
for i in range(42):
    images.append(PhotoImage(file='./Fiche GUI Tkinter/imagesLaszlo/image-'+str(i)+'.gif'))

x,y,dx,dy,img = 300,300,0,0,0
perso = Fond.create_image(x,y, image=images[0])


speed = 20


def up(*args):
    Fond.move(perso,0,-speed)
    cur_coords = Fond.coords(perso)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[1] <= -15:
        Fond.move(perso,0,555)

def down(*args):
    Fond.move(perso,0,speed)
    cur_coords = Fond.coords(perso)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[1] >= 550.0:
        Fond.move(perso,0,-555)

def left(*args):
    Fond.move(perso,-speed,0)
    cur_coords = Fond.coords(perso)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[0] <= -15:
        Fond.move(perso,565,0)

def right(*args):
    Fond.move(perso,speed,0)
    cur_coords = Fond.coords(perso)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[0] >= 550.0:
        Fond.move(perso,-555,0)

#BONHOMME BOUGE.


fenetre.bind("<KeyPress-Up>", up)
fenetre.bind("<KeyPress-Down>", down)
fenetre.bind("<KeyPress-Left>", left)
fenetre.bind("<KeyPress-Right>", right)


fenetre.mainloop()