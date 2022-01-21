
#Déclaration des constantes
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


print("**********************")
print("* Machine ENIGNMA M3 *")
print("**********************")

#INITIALISATION DES ELEMENTS
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


#rotation
def rotation(Irot,n=1):
    Irot= Irot[n:]+Irot[:n]
    return(Irot)

initour = []
for i in range(3):
    initour.append(ALPHABET.index(posRotors[i]))
    rotors123[i] = rotation(rotors123[i], initour[i])
    print("Rotor {} en position {} --> {}".format(choixRotors[i], i+1, rotors123[i]))
print("Réflecteur {} --> {}".format(lRef, REFLECTEURS[nRef]))
print("cablage : ", cables)

#connecteurs

def connecteurs(car,cablage_num):
    carcode=""
    if ALPHABET.index(car) in cablage_num:
        indice=cablage_num.index(ALPHABET.index(car))
        if indice%2==0:
            carcode= ALPHABET[cablage_num[indice+1]]
        else:
            carcode= ALPHABET[cablage_num[indice-1]]
    else:
        carcode=car
#rotor
def rotor(car,lrot):
    return lrot[ALPHABET.index(car)]


#rechAlphabet
def rechAlphabet(ltr,lst,deca):
    return  ALPHABET[(lst.index(ltr))+(deca%26)]