import tkinter as Tk

fenetre = Tk.Tk()

canvas = Tk.Canvas(fenetre, height=100, width=200)
canvas.pack()

oval = canvas.create_oval(20,20,70,70, width=2, fill='red')
rect = canvas.create_rectangle(90,20,140,70, width=2, fill='green')
poly = canvas.create_polygon([160,45,175,20,190,45,175,70], width=2, fill='blue')

def ColorChange():
    canvas.itemconfigure(oval, fill='blue')  
    canvas.itemconfigure(rect, fill='#67A12B')
    canvas.itemconfigure(rect, fill='#001020')

btn = Tk.Button(fenetre, text='Changer la couleur des objets', command= ColorChange)
btn.pack()

fenetre.mainloop()

