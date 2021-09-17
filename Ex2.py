import random

#On définit le nombre nb compris entre 1 et 30 que l'utilisateur doit retrouver.
nb = random.randint(1, 30)


#----------------------Présentation *jolie* pour le terminal.-----------------------#

print()
print("+----------------------------------------------------------------------+")
print("J'ai choisi un nombre entre 1 et 30, a toi de le retrouver en 5 essais !")
print("+----------------------------------------------------------------------+")
print()

#------------------------------------------------------------------------------------#



#------------------Boucle des 5 demandes de nombre à l'utilisateur.--------------------------#

for i in range(5):
    #str(i+1) pour que le nombre soit convertit en string et soit accepté par la fonction print().
    print("+--+ Proposition n° " + str(i+1) + " +--+")
    
    propo = int(input("Votre proposition : "))

    #Vérifie que la proposition est comprise entre 1 et 30.
    if propo < 1 or propo > 30 :
        print("Entrer un nombre compris entre 1 et 30...")
    

    #Si la proposition est supérieurs au nombre
    elif nb < propo :
        print()
        print("Trop grand !")
        print()

    #Si la proposition est inférieur au nombre
    elif nb > propo :
        print()
        print("Trop petit !")
        print()

    #Si la proposition est égal au nombre
    elif nb == propo :
        print("Bravo, c'était bien " + str(nb) +" ! Vous avez trouvez en " + str(i+1) + " essais.")
        
        #break sauvage!!!!(Peu recommendé)
        break
        
        
    #Lorsque l'utilisateur a essayé 5 fois, la réponse est donnée et le programme est terminé.
    if i+1 == 5 :
        print("Dommage, c'était " + str(nb) + ".")