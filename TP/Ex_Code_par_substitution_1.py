txtcode = "42 14 23 24 33 11 21 14 25 34 12 23 42 24 45 14 44 13 21"
carre = [['L','O','U','I','S'],['E','G','R','A','N'],['D','B','C','F','H'],['K','M','P','Q','T'],['V','W','X','Y','Z']]
txtcode = txtcode.replace(" ","")
txt = ""
char=""
a=0

for i in range(len(txtcode)):
    a+=1 
    if a%2 == 1:
        char = carre[int(txtcode[i])-1][int(txtcode[i+1])-1]
        txt += char
print(txt)