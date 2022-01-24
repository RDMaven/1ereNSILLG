from tkinter import *
from random import random

root = Tk()
can = Canvas(root, width=400, height=400, bg="white")
can.pack()

def collect(id):
    can.delete(id)

for i in range(1):
    x = round(random()*380)
    y = round(random()*380)
    id=can.create_oval(x, y, x+20, y+20, fill="yellow")
    can.tag_bind(id, "<Button-1>", lambda event, j=id: collect(j))
    co_p = [x,y,x+20,y+20]
    print(co_p)

root.mainloop()