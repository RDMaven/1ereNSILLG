msgPerseverance4 = "00001000100000001011000011101000000011100001110110000000101000000111110000010111"
coord = []
n = 0

while len(msgPerseverance4) > 0:
    msgPerseverance4 = msgPerseverance4[3:]
    
    if n%2 != 0 :
        #msgPerseverance4 = msgPerseverance4[7:]
        carcercle = str(int(msgPerseverance4[:7]))
    else :
        carcercle = chr(int(msgPerseverance4[:7], 2) + 64)
    coord += carcercle
    msgPerseverance4 = msgPerseverance4[7:]
    #coord += " "
    n+=1

print(coord)



