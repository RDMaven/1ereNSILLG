from IPython.display import IFrame

src = "https://peertube.monlycee.net/videos/watch/589742d9-79c8-4110-bf83-a0cb72865ab7"
IFrame(src, 620, 400)

#+-------------------------------------+# Déclaration des constantes
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##Description des cinq rotors de la machine (Codage historique)
ROTORS = ('EKMFLGDQVZNTOWYHXUSPAIBRCJ',
        'AJDKSIRUXBLHWTMCQGZNPYFVOE',
        'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        'ESOVPZJAYQUIRHXLNFTGKDCMWB',
        'VZBRGITYUPSDNHLXAWMJQOFECK')
##Encoches sur chaque rotor pour basculer le suivant
ENCOCHES = ("Q", "E", "V", "J", "Z")
##Description des deux réflecteurs (Codage historique)
REFLECTEURS = ('YRUHQSLDPXNGOKMIEBFZCWVJAT', 'RDOBJNTKVEHMLFCWZAXGYIPSUQ')
#+-------------------------------------+#

print("**********************")
print("* Machine ENIGNMA M3 *")
print("**********************")

def rotation(lrot, n=1):
    return lrot[n:] + lrot[:n]

rotation(ALPHABET, 4)
print(ALPHABET)

#Vérification de la fonction rotation.
assert rotation(ALPHABET, 4) == 'EFGHIJKLMNOPQRSTUVWXYZABCD', "Essaye encore !"


