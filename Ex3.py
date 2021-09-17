#!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!#
#Cette méthode est peut-être la méthode demandée par Josse : la phrase n'est pas transformée en liste...
#!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!#



#=====================================================================================================#
#=========================================PARTIE 1, Ex3===============================================#
#=====================================================================================================#


#----------------------Présentation *jolie* pour le terminal.-----------------------#
print()
print("+----------------+ Encoding Start +----------------+")
print()

#------------------------------------------------------------------------------------#



#--------------------------------------------------------------------------------------#
#--------------------Définitions PHRASE, CODE et PHRASE FINALE ------------------------#
#--------------------------------------------------------------------------------------#

phrase = input("Entrer votre phrase : ")
code = input("Entrer le code : ")

code_list = []



#Code -> liste de charactères.# (pour chaque charactère dans le code, mettre un charactère à la position i dans la liste code_list.)
for i in code : 
    code_list.append(i)


phrase_finale = ""
phrase_finale_list = []



print()
print()

#------------------------------------------------------------------------------#
#--------------------Encoding de la phrase avec le code------------------------#
#------------------------------------------------------------------------------#

#   Pour chaque caractère dans la phrase,
#       - On ajoute le caractère à la iéme position de la PHRASE *DANS* la liste de la phrase finale,
#       - On ajoute un caractère à la "index_char_code"éme position de la liste du CODE *DANS* la liste de la phrase finale,
#       - On ajoute 1 à "index_char_code" pour qu'on ait le charactère suivant du CODE.

#       - On vérifie que "index_char_code" n'a pas dépassé la longueure de la liste du CODE.
#           - SI OUI : On remet l'index à 0.
#           - SI NON : On continue la boucle.


index_char_code = 0

for i in phrase :

    phrase_finale_list.append(i)
    phrase_finale_list.append(code_list[index_char_code])

    index_char_code += 1

    if index_char_code == len(code_list) :
        index_char_code = 0


#--Rassemblage de la liste "phrase_finale_liste" en phase.--#

for i in phrase_finale_list:
    phrase_finale += i




#-------- RESULTAT----------#

print("Votre phrase codée : " + phrase_finale)
print()
print("+----------------+ Encoding Finished +----------------+")
print()
#---------------------------#


#=====================================================================================================#
#=========================================PARTIE 2, Ex4===============================================#
#=====================================================================================================#

input("Press Enter to continue...")


#----------------------Présentation *jolie* pour le terminal.-----------------------#

print()
print("+--------------------------------------+")
print("|      Je vais décoder la phrase :     |")
print("        ==>    "+ phrase_finale)
print("+--------------------------------------+")
print()

#-----------------------------------------------------------------------------------#

input("Press Enter to continue...")

#------------------------------------------------------------------#
#--------------------Decoding de la phrase ------------------------#
#------------------------------------------------------------------#


#Pour décoder la phrase, on utilise le fait que une fois sur 2, le caractère est de la phrase en partant de 0.#
#   - On doit enlever les caractères a indexes 1,3,5,7,9,...
#   - MAIS, lorsqu'on enlève un caractère à la liste, l'index des caractères suivant sont diminués de 1.
#   - DONC, on doit enlever les caractères en partant de 1 et ajouter 1 à chaque fois.


#--Définitions : --#
phrase_decoded_list = []


for i in phrase_finale :
    phrase_decoded_list += i

#=----------------#

#Les caractères de la phrase forment 1/2 de la list, on va donc travailler sur la moité de la list :

len_phrase_decoded = len(phrase_decoded_list)
half_len_phrase = round(len_phrase_decoded/2)-1
#-----------------#


index_phrase = 1
del phrase_decoded_list[index_phrase]

for i in range(half_len_phrase):

    index_phrase += 1
    del phrase_decoded_list[index_phrase]


#--Rassemblage de la liste "phrase_decoded_list" en phase.--#

phrase_decoded = ""

for i in phrase_decoded_list:
    phrase_decoded += i




#-------- RESULTAT----------#

print("Votre phrase décodée : " + phrase_decoded)
print()
print("+---------+ Decoding Finished +---------+")
print()
#---------------------------#
