
import	math

#----------------Demandes des valeurs à l'utilisateur.-------------------------#
moteur = float(input("Entrer la vitesse de rotation du moteur (tr/min) : "))
roue = float(input("Entrer le diamètre de la roue (mm) : "))
#------------------------------------------------------------------------------#

#Équation : Vitesse = (tr/min (diamètre[mètres] * PI) / 60). Arrondi à deux décimales avec round()
vitesse_ms = round(moteur * roue/1000 * math.pi / 60, 2)

#Conversion en km/h...
vitesse_kmh = vitesse_ms * 3600/1000

#Résultat.
print("Le véhicule se déplace à une vitesse de " + str(vitesse_ms) + "m/s, soit " + str(vitesse_kmh) + "km/h.")


