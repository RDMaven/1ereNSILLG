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

#+-------------------------------------+# INITIALISATION DES ELEMENTS
##Choix des 3 rotors parmi les 5
print("\nChoisir 3 rotors parmi les 5 : 1, 2, 3, 4 ou 5 :")
choixRotors = [None, None, None]
rotors123 = []
encoches123 = []
for i in range(3):
    choixRotors[i] = int(input("Choix rotor n°" + str(i + 1) + " : "))
    assert choixRotors[i] > 0 and choixRotors[i] < 6
    rotors123.append(ROTORS[choixRotors[i]-1])
    encoches123.append(ENCOCHES[choixRotors[i]-1])

##Position initiale des rotors choisis
print("\nPosition des rotors")
posRotors = [None, None, None]
for i in range(3):
    posRotors[i] = input("Saisir la 'lettre' initiale du rotor " + str(i + 1) + " choisi : ").upper()
    assert posRotors[i] in ALPHABET
    
##Choix du réflecteur parmi les deux
print("\nChoisir le reflecteur")
nRef = 0
lRef = input("\nSaisir le réflecteur (B ou C) : ").upper()
if lRef=="C":
    nRef = 1

##Tableau de connexions
cablage_num = []
cables = input("\nEntrez le câblage (6 paires de lettres Max) sous forme d'une chaîne de 12 lettres Max sans espace : ").upper()
cablage_num = [ALPHABET.index(c) for c in cables]
assert len(cablage_num) <= 12, "trop de connecteurs utilisés"
assert len(cablage_num)%2 == 0, "il faut connecter des paires de lettres"

##Le message à décoder
message = input("\nSaisir le message à coder : ").upper()
for i in message: assert i in ALPHABET, "utiliser uniquement les lettres de l'alphabet"

##Le message codé, initialement vide
message_code = ''
#+-------------------------------------+#

##Fonction rotation : rotation à gauche de la chaîne de caractères alphabétiques lrot, de n caractères.Vaut 1 par défaut.

def rotation(lrot, n=1):
    return lrot[n:] + lrot[:n]

rotation(ALPHABET, 4)
print()

#Vérification de la fonction rotation.
assert rotation(ALPHABET, 4) == 'EFGHIJKLMNOPQRSTUVWXYZABCD', "Essaye encore !"


initour = []
for i in range(3):
    initour.append(ALPHABET.index(posRotors[i]))
    rotors123[i] = rotation(rotors123[i], initour[i])
    print("Rotor {} en position {} --> {}".format(choixRotors[i], i+1, rotors123[i]))
print("Réflecteur {} --> {}".format(lRef, REFLECTEURS[nRef]))
print("cablage : ", cables)



#Fonction connecteurs: échange lettres connectées sur le tableau avant. max : 6 paires. 

"""def connecteurs (car, cablage_num):
    for i in range(len(cablage_num)):
        if ALPHABET.index(car) == cablage_num[i]:
            if i%2==0:
                return ALPHABET[cablage_num[i+1]]
            else:
                return ALPHABET[cablage_num[i-1]]
    return car """
        
def connecteurs (car, cablage_num):
    idl = ALPHABET.index(car)
    if idl not in cablage_num:
        return car
    else:
        idc = cablage_num.index(idl)
        if idc%2 ==1:
            return ALPHABET[cablage_num[idc-1]]
        else:
            return ALPHABET[cablage_num[idc+1]]

assert connecteurs("A", [0, 25, 4, 17, 19, 24]) == "Z"
assert connecteurs("Y", [0, 25, 4, 17, 19, 24]) == "T"


def rotor(car,lrot):
    return lrot[ALPHABET.index(car)]

assert rotor("B", ROTORS[0]) == "K"

#Fonction rechAlphabet qui cherche la position de la lettre "ltr" dans la liste "lst" en appliquant un décalage "decal" correspondant au nombre de pas d'un rotor. Attention, ce nombre peut être supérieur aux 26 lettres de l'alphabet.

def rechAlphabet(car,lst, decal):
"""    print("armand")
    for i in "armand":
        for c in range(10):
            print(i)    
"""
        
assert rechAlphabet("A", ALPHABET, 27) == "B"
assert rechAlphabet("A", ROTORS[0], 27) == "V"
assert rechAlphabet("A", ROTORS[2], 27) == "U"
