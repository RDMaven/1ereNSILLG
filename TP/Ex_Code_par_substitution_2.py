txtcode = ""
conv = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
decalage = 3
mot = "azerty"

for i in range(26):
        conv[alphabet[i]]= alphabet[(i+decalage)%26]

for t in mot:
    txtcode = txtcode + conv[t]

print(conv)
assert txtcode == "dchuwb", "Ce code n'est pas correct !"
print(f"{mot} --> {txtcode}")