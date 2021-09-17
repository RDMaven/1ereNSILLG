
#Input Phrase + split Phrase
print()
print("+----------------+ Encoding Start +----------------+")
print()
phrase = input("Entrer votre phrase : ")

chars_phrase = []

for i in phrase : 
    chars_phrase.append(i)

#print("chars_phrase is : " + str(chars_phrase))

#Input Code + split Code
print()
code = input("Entrer le code : ")
print()

chars_code = []
for i in code : 
    chars_code.append(i)

#print("chars_code is : "+ str(chars_code))

#Encoding
nb = 0
final_phrase = ""
encoded_phrase = []
for i in phrase :
    encoded_phrase.append(i)
    encoded_phrase.append(chars_code[nb])
    nb += 1
    if nb == len(chars_code) :
        nb = 0
#print(encoded_phrase)

for i in encoded_phrase:
    final_phrase += i


print("Votre phrase codée : " + final_phrase)



print("+----------------+ Encoding Finished +----------------+")

#Décoder

decoded_chars = []
decoded_code = []
for i in final_phrase :
    decoded_chars += i
    decoded_code += i
print(decoded_chars)

nb = 1

del decoded_chars[nb]
del decoded_code[nb-1]
half_chars = len(decoded_chars)/2
print(len(decoded_chars))
print("half_chars is =" + str(half_chars))
half_chars = round(half_chars)-1
print("half_chars is =" + str(half_chars))

for i in range(half_chars):
    
    del decoded_chars[nb+1]
    del decoded_code[nb]
    nb += 1
print(decoded_chars)
print(decoded_code)

decoded_phrase = ""
decoded_code_f = ""
for i in decoded_chars:
    decoded_phrase += i

for i in decoded_code:
    decoded_code_f += i
print(decoded_phrase)
print(decoded_code_f)

final_code = ""
for i in decoded_code_f :
    final_code += i
    nb_codes = decoded_code_f.count(final_code)
    if nb_codes == 1:
        print(final_code)
        
        break


