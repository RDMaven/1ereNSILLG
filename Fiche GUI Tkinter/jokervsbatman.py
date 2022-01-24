# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:17:56 2022

@author: NSI
"""
import tkinter as Tk
fenetre = Tk.Tk()
canvas = Tk.Canvas(fenetre, height=300, width=300, bg='white')
canvas.pack()
oreille1= canvas.create_polygon(55,20,55,120,70,120,60,60,fill='white')
oreille2=canvas.create_polygon(245,20,245,120,230,120,245,60,fill='white')
visage=canvas.create_oval(50,50,250,250,width=1,fill='green')
canvas.create_oval(75,100,135,135,width=0,fill='white')
canvas.create_oval(165,100,225,135,width=0,fill='white')
bouche=canvas.create_arc(80,120,220,210,width=12,outline='red',fill='white',start=180,extent=180)

def ColorChange():
    cur_color = canvas.itemcget(visage, "fill")

    if cur_color == 'green' :
        canvas.itemconfig(visage, fill = "black")
        canvas.itemconfig(oreille1,fill='black')
        canvas.itemconfig(oreille2,fill='black')
        canvas.itemconfig(bouche,outline='black')
    else:
        canvas.itemconfig(oreille1,fill='white')
        canvas.itemconfig(oreille2,fill='white')
        canvas.itemconfig(visage, fill='green')  
        canvas.itemconfig(bouche,outline='red')
      
btn = Tk.Button(fenetre, text = "JokerVSBatman", command = ColorChange)
btn.pack()
fenetre.mainloop()
