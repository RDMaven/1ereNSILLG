from pyfirmata2 import Arduino
import time
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