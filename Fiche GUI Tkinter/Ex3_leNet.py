
# imports every file form tkinter and tkinter.ttk
from calendar import c
from tkinter import *
from tkinter.ttk import *
import time
from matplotlib.pyplot import fill
 
class GFG:
    def __init__(self, master = None):
        self.master = master
        self.x = 1
        self.y = 0
        self.stopVar = 1
 
        # canvas object to create shape
        self.canvas = Canvas(master, width=400, height=400)
        # creating rectangle
        self.sq_dim = 30
        self.rectangle = self.canvas.create_rectangle(5, 5,5+self.sq_dim,5+self.sq_dim, fill = "red")
        self.pause_msg = self.canvas.create_text(200, 400-20, text="Press any movement key to continue.", font="Arial 16 italic", fill="red")
        self.fail_msg = self.canvas.create_text(200,200-20,text="", font="Arial 16 italic", fill="red")
        self.canvas.pack()
 
        self.movement()


    def movement(self):
        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.after(25, self.movement)
        self.cur_coords = self.canvas.coords(self.rectangle)

        #If the object is moving
        if self.stopVar == 1:
            #display coordinates
            print(f"Current coords = [{self.cur_coords[0]}, {self.cur_coords[1]}]")
            
     
    def left(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = -5
        self.y = 0
        self.stopVar = 1
             
    def right(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = 5
        self.y = 0
        self.stopVar = 1
     
    def up(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = 0
        self.y = -5
        self.stopVar = 1

    def down(self, event):
        self.canvas.delete(self.pause_msg)
        #if self.stopVar == 0 | self.stopVar == 1:
        self.x = 0
        self.y = 5
        self.stopVar = 1
 
    def pause(self, event):
        if self.stopVar == 1:
            self.x = 0
            self.y = 0
            self.stopVar = 0
            self.pause_msg = self.canvas.create_text(200, 400-20, text="Press any movement key to continue.", font="Arial 16 italic", fill="red")


    def reset(self, event):
        self.canvas.delete(self.rectangle)
        self.canvas.delete(self.pause_msg)
        self.canvas.delete(self.fail_msg)
        self.x = 1
        self.y = 0
        self.stopVar = 1
        self.rectangle = self.canvas.create_rectangle(5, 5,5+self.sq_dim,5+self.sq_dim, fill = "red")




if __name__ == "__main__":
    master = Tk()
    gfg = GFG(master)

    master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
    master.bind("<KeyPress-space>", lambda e: gfg.pause(e))
    master.bind("<KeyPress-r>", lambda e: gfg.reset(e))

            #if the rectangle is out of the screen.
    """if (round(gfg.cur_coords[0]+self.sq_dim) >= 400) | (round(self.cur_coords[0]) <= 0) | (round(self.cur_coords[1]+self.sq_dim) >= 400) | (round(self.cur_coords[1]) <= 0)  :
        self.canvas.itemconfig(self.fail_msg, text="Game Over. 3s")
        self.x = 0
        self.y = 0
        self.stopVar = 2"""
    

    # Infinite loop breaks only by interrupt
    mainloop()