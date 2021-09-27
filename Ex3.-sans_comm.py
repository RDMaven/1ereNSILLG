#=====================================================================================================#
#=========================================PARTIE 1, Ex3===============================================#
#=====================================================================================================#

print()
print("+----------------+ Encoding Start +----------------+")
print()

phrase = input("Entrer votre phrase : ")
code = input("Entrer le code : ")
code_list = []
for i in code : 
    code_list.append(i)
phrase_finale = ""
phrase_finale_list = []
print()
print()
index_char_code = 0
for i in phrase :
    phrase_finale_list.append(i)
    phrase_finale_list.append(code_list[index_char_code])
    index_char_code += 1
    if index_char_code == len(code_list) :
        index_char_code = 0
for i in phrase_finale_list:
    phrase_finale += i
print("Votre phrase codée : " + phrase_finale)
print()
print("+----------------+ Encoding Finished +----------------+")
print()

#=====================================================================================================#
#=========================================PARTIE 2, Ex4===============================================#
#=====================================================================================================#

input("Press Enter to continue...")
print()
print("+--------------------------------------+")
print("|      Je vais décoder la phrase :     |")
print("        ==>    "+ phrase_finale)
print("+--------------------------------------+")
print()
input("Press Enter to continue...")
phrase_decoded_list = []
for i in phrase_finale :
    phrase_decoded_list += i
len_phrase_decoded = len(phrase_decoded_list)
half_len_phrase = round(len_phrase_decoded/2)-1
index_phrase = 1
del phrase_decoded_list[index_phrase]
for i in range(half_len_phrase):
    index_phrase += 1
    del phrase_decoded_list[index_phrase]
phrase_decoded = ""
for i in phrase_decoded_list:
    phrase_decoded += i
print("Votre phrase décodée : " + phrase_decoded)
print()
print("+---------+ Decoding Finished +---------+")
print()
