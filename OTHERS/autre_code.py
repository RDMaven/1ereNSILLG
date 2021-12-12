txtcode = ""

def cesar(txt, decalage):
    secret=""
    for i in range(len(txt)):
        char = chr(ord(txt[i])+decalage)
        secret += char
    return secret

txt = "Ave, César !"
dec = 3
txtcode = cesar(txt, dec)
assert txtcode == "Dyh/#Fìvdu#$", "Ce code n'est pas correct !"
print(f"{txt} --> {txtcode}")


#insert code

#encode


#détermine les coefs

#rend la clé (ensemble des coefs)
