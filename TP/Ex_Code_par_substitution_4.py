# Proposer une fonction "vigenere" qui prend en paramètre le texte en clair 
# ainsi que la clé et qui renvoie le texte chiffré en respectant majuscules et minuscules. 
# Les caractères autres qu'alphabétiques ne seront pas chiffrés.


def vigenere(txt, cle):

    mot = ""
    
    for i in range(len(txt)):
        
        est_une_min = ord(txt[i]) in range(97,122)
        est_une_maj = ord(txt[i]) in range(65,90)
        est_autre = not est_une_maj and not est_une_min
        
        if est_une_min or est_une_maj: #SI C'EST UNE MINUSCULE OU UNE MAJUSCULE
            if est_une_min: position_a = 97
            elif est_une_maj: position_a = 65
    
            place_abc_char_txt_i = ord( txt[i] )-position_a
            place_abc_char_cle_i = ord( cle[i % (len(cle) )] )-position_a
            
            place_abc_char_code = place_abc_char_txt_i + place_abc_char_cle_i
            
            char_code = chr((place_abc_char_code%26) + position_a)
    
        elif est_autre: #SI C'EST AUTRE CHOSE
            
            char_code = txt[i]

        mot += char_code
    

    # renvoyer mot
    return mot


txt = "Chiffrement de vigenère"
cle = "azerty"
txtcode = vigenere(txt, cle)

assert txtcode == "Igmwypeliem dd mbeemèix", "Ce code n'est pas correct !"
print(f"(clé = {cle}) --> {txtcode}")