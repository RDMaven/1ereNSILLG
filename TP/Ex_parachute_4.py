msgPerseverance4 = ["00001000100000001011000011101000000011100001110110000000101000000111110000010111"]

code = ""
a = 0
#Début

for cercle in msgPerseverance4:
    #Tant qu'il reste des caractères dans le cercle faire
    while len(cercle) > 0:

        #Supprimer les trois premiers bits 000
        cercle = cercle[3:]

        #Traduire le caractère codé sur ces sept bits
        carcercle = chr(int(cercle[:7], 2) + 64)

        #Si ce n'est pas un point cardinal
        cardinale_y_n = carcercle.lower() == "n" or carcercle.lower() == "s" or carcercle.lower() == "e" or carcercle.lower() == "w"
        
        if not cardinale_y_n :

            #Traduire le chiffre codé sur les sept bits suivants (!! ERREUR DANS LA CONSIGNE : pas les bits SUIVANTs mais les mêmes bits qui n'est pas point cardinal.)
            carcercle = int(cercle[0:7], 2)

            #Sauvegarder le caractère
            code += str(carcercle)
            
            #Ajout des caractères : ° ; ' ; "

            a += 1

            if a == 1 or a == 4:
                code += "°"
            elif a == 2 or a == 5:
                code += "'"
            else :
                code += '" '
        
        #BONUS : ajouter un espace pour la présentation.
        else :
            #Sauvegarder le caractère
            code += str(carcercle)

            code += " "

        #Retirer le caractère du cercle
        cercle = cercle[7:]

    #Afficher le code
print(code)

#Fin