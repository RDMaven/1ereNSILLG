#Libs
import tkinter as Tk

#Init
fenetre = Tk.Tk()

# canvas
canvas = Tk.Canvas(fenetre, height=500, width=300)
ligne1 = canvas.create_line(150,0,150,500, dash=(4,4))
ligne2 = canvas.create_line(0,250,300,250)
rect = canvas.create_rectangle(140,240, 160, 260, width=2, fill='pink')

#defs
speed = 100
tour = 0

def ups(*args):
    canvas.move(rect,0,-speed)
    cur_coords = canvas.coords(rect)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[1] <= -15:
        canvas.move(rect,0,505)
        tour = 1
        print(tour)

def downs(*args):
    canvas.move(rect,0,speed)
    cur_coords = canvas.coords(rect)
    #print(f"Current coords = [{cur_coords[0]}, {cur_coords[1]}]")
    if cur_coords[1] >= 495.0:
        canvas.move(rect,0,-505)
        tour = 1
        print(tour)


def mouseM(event):
    if event.delta == 120:
        ups()

    if event.delta == -120:
        downs()
    
canvas.pack()


btnM = Tk.Button(fenetre, text='Monter', command=ups)
btnD = Tk.Button(fenetre, text='Descendre', command=downs)
btnM.pack()
btnD.pack()


fenetre.bind("<KeyPress-Up>", ups)
fenetre.bind("<KeyPress-Down>", downs)
fenetre.bind('<MouseWheel>', mouseM)

fenetre.mainloop()