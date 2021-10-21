msgPerseverance123 = ["0000000100000000000100000100100000000101", "000000110100000010010000000111000000100000000101000000011001","000001010000000010000000001001000000111000000001110000010011"]
code = ""

for cercle in msgPerseverance123:
    while len(cercle) > 0:
        cercle = cercle[3:]
        carcercle = chr(int(cercle[:7], 2) + 64)
        code += carcercle
        cercle = cercle[7:]
    code += " "

print(code)



