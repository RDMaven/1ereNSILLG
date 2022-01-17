import tkinter as Tk

fenetre = Tk.Tk()

canvas = Tk.Canvas(fenetre, height=300, width=300)
canvas.pack()

cXL = 50
cYL = 50
cXR = cXL + 200
cYR = cYL + 200
milieu_X = (cXR-cXL)/2+cXL
smile_Y = 180

print(milieu_X)

oval = canvas.create_oval(cXL,cYL,cXR,cYR, width=2, fill='yellow')

eye_l = canvas.create_oval(cXL+20,cYL+50,cXL+35,cYL+65, width=2, fill='black')
eye_l = canvas.create_oval(cXR-20,cYL+50,cXR-35,cYL+65, width=2, fill='black')

smile = canvas.create_line(
    milieu_X-80,smile_Y-30,
    milieu_X-50,smile_Y,
    milieu_X,smile_Y,
    milieu_X+50, smile_Y,
    milieu_X+80, smile_Y-30,
    width=3
    )


canvas.itemcget(oval, "fill")

def MoodChange():
    cur_color = canvas.itemcget(oval, "fill")

    if cur_color == "yellow":
        canvas.itemconfigure(oval, fill='red')
        canvas.coords(smile, 
            milieu_X-80,smile_Y+30,
            milieu_X-50,smile_Y,
            milieu_X,smile_Y,
            milieu_X+50, smile_Y,
            milieu_X+80, smile_Y+30
        )

    elif cur_color == "red":
        canvas.itemconfigure(oval, fill='yellow')
        canvas.coords(smile, 
            milieu_X-80,smile_Y-30,
            milieu_X-50,smile_Y,
            milieu_X,smile_Y,
            milieu_X+50, smile_Y,
            milieu_X+80, smile_Y-30
        )



btn = Tk.Button(fenetre, text='Changer la couleur des objets', command= MoodChange)
btn.pack()

fenetre.mainloop()

