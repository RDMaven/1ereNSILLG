#import #serial
from os import close
import time
from tkinter import *
from pyfirmata2 import Arduino

fenetre1 = Tk()

#CONFIG FENETRE 1
#fenetre1.geometry('300x200')
fenetre1.title("Exercice 1")
#################

#NON ELEMENTS


"""
try:
    macarte = Arduino('COM7')
except:
    print("Problème de liaison avec Arduino")
    liaison = False
else:
    macarte.samplingOn()
    servo = macarte.get_pin("d:5:s")
    potar = macarte.get_pin("a:0:i")
    led = macarte.get_pin("d:3:o")
    bp = macarte.get_pin("d:4:i")
    time.sleep(0.03)
    angleservo = 90
    servo.write(angleservo)
    time.sleep(1)
    liaison = True
if liaison==True:
    for i in range(50) :
        print("A0 : {:.2f}V".format(potar.read()*5))
        time.sleep(0.2)
        val_bp = bp.read()
        if val_bp==True :
            led.write(1)
            print("bp : on")
            time.sleep(1)
        else :
            led.write(0)
            print("bp : off")
    macarte.exit()
print("Arrêt du programme")
"""

#################

#ELEMENTS

    #BUTTONS
button1 = Button(fenetre1, text='On', activebackground='green', width=5, height=2)
button2 = Button(fenetre1, text='Off', activebackground='red', width=5, height=2)
button3 = Button(fenetre1, text='Exit', activebackground='red', background='red', width=5, justify='center', pady=2, command=fenetre1.quit) #command=Arduino('COM7').exit())
#GRIDS
button1.grid(row=0, column=1)
button2.grid(row=1, column=1)
button3.grid(row=0, column=10, sticky=NE)




    #TEXT
txt1 = Label(fenetre1, text="A0 : ..V", font=("Courier", 14,'bold')) #.format(potar.read()*5)
txt2 = Label(fenetre1, text="  Bp = ", font=("Courier", 14,'bold'))
#GRIDS
txt1.grid(row=0, column=2)
txt2.grid(row=1, column=2)



no_txt1 = Label(fenetre1, text="", width=3)
no_txt2 = Label(fenetre1, text="", width=3)
no_txt3 = Label(fenetre1, text="", width=3)
no_txt4 = Label(fenetre1, text="", width=3)
#GRIDS
no_txt1.grid(row=100, column=2)
no_txt2.grid(row=100, column=3)
no_txt3.grid(row=100, column=4)
no_txt4.grid(row=100, column=5)

#################







fenetre1.mainloop()
#################