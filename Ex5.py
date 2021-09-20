import inquirer

print()
print("+------------------------------------------------------------------+")
print("| Déterminons la valeur de la résistance à 3 couleurs + tolérance. |")
print("+------------------------------------------------------------------+")
print()

couleur = {"noir":0,"marron":1, "rouge":2, "orange":3, "jaune":4, "vert":5, "bleu":6, "violet":7, "gris":8, "blanc":9, "or":"5%", "argent":"10%"}
print("Les couleurs sont : " + str(couleur.keys()) + ".")


for i in range(3):
  print()
  exec("A"+str(i+1)+" = input('Valeur A"+str((i+1))+" : ').lower()")
  exec("A"+str(i+1)+"_val = "+ str(couleur[eval("A"+str(i+1))]))

print()
A4 = input("la tolérance : (or, argent) : ").lower()

print()
R = (A1_val*10 + A2_val)*10**A3_val
print("la résisstance est de : " + str(R) + " Ω " + couleur[A4])
print()
vf = input("voulez-vous convertir en kΩ ? (y/n) : " )
print()
if vf == 'y':
  R = R/1000
  print("La résistance est de : "+ str(R) + "kΩ")
else :
  print("Done.")