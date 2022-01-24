import tkinter as Tk

fenetre = Tk.Tk()

canvas = Tk.Canvas(fenetre, height=500, width=300)



# canvas
ligne1 = canvas.create_line(150,0,150,500, dash=(4,4))
ligne2 = canvas.create_line(0,250,300,250)

rect = canvas.create_rectangle(140,240, 160, 260, width=2, fill='pink')

def ups(event):
    canvas.move(rect,0,-10)

def downs(event):
    canvas.move(rect,0,10)
    canvas.after(100, canvas.move(rect,0,10))

canvas.pack()



btnM = Tk.Button(fenetre, text='Monter', command=ups)
btnM.pack()
btnD = Tk.Button(fenetre, text='Descendre', command=downs)
btnD.pack()


fenetre.bind("<KeyPress-Up>", ups)
fenetre.bind("<KeyPress-Down>", downs)


fenetre.mainloop()