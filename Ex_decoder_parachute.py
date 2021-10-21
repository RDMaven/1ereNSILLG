#msgBin = ["0000000100000000000100000100100000000101", "000000110100000010010000000111000000100000000101000000011001","000001010000000010000000001001000000111000000001110000010011"]
msgBin = ["0000000100000000000100000100100000000101"]



for i in msgBin:
    chars = list(i)

lenList = print(int(len(chars))/8)
#for j in range(lenList):

z = 0

strList = chars[0+z:8]
str = "000"+''.join(str(elem) for elem in strList) 
print(str)


print(chars[0+z:8])
print(chars[8+z:16])
print(chars[16+z:24])
print(chars[24+z:32])
print(chars[32+z:40])



"""Début
Pour chaque cercle Faire
Tant qu'il reste des caractères dans le cercle faire
Supprimer les trois premiers bits 000
Traduire le caractère codé sur les sept bits suivants
Sauvegarder le caractère
Retirer le caractère du cercle
Ajouter un espace pour séparer les messages
Afficher le code
Fin"""







