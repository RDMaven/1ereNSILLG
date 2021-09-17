#Équation : Vitesse = (tr/min (diamètre * PI) / 60)
import	math


moteur = float(input("Entrer la vitesse de rotation du moteur (tr/min) : "))
roue = float(input("Entrer le diamètre de la roue (mm) : "))

vitesse_ms = round(moteur * roue/1000 * math.pi / 60, 2)

vitesse_kmh = vitesse_ms * 3600/1000

print("Le véhicule se déplace à une vitesse de " + str(vitesse_ms) + "m/s, soit " + str(vitesse_kmh) + "km/h.")


