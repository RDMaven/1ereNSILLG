def charger_data():
    #fonction qui permet de lire et d'organiser la liste des pokemons"
    #sortie : une lsite de 
    pokedex=[] #liste qui contiendra des dictionnaires pour chaque pokemon
    fichier=open('pokemon.csv','r')
    categorie=fichier.readline().strip().split(';') #liste des categories 
    liste=fichier.read().strip().split('\n') #liste de tous les pokemons
    
    for loop in liste: #on parcourt la liste
        loop=loop.split(';')
        pokedex.append({categorie[0]:loop[0],categorie[1]:int(loop[1]),categorie[2]:int(loop[2]),categorie[3]:int(loop[3]),categorie[4]:int(loop[4]),categorie[5]:loop[5]})
    
    return pokedex

assert charger_data()[0] == {'nom': 'Clic', 'points de vie': 60, 'attaque': 80, 'defense': 95, 'vitesse': 50, 'type': 'Acier'}
#on teste le resultat pour la première ligne



def distance(pok1,pok2):
    #entrees: deux dictionnaires de pokemons 
    #sortie : la distance entre les deux pokemons
    a=0
    for loop in pok1.keys():
        if loop != "nom" and loop != "type":  #on enlève les deux catégories à ne pas prendre en compte
            a=a+abs(pok1[loop]-pok2[loop])    #calcul de la distance
    return a

assert distance( charger_data()[0], charger_data()[1])==80


nouv= {'nom': 'Hippodocus ', 'points de vie': 108, 'attaque': 112, 'defense': 118, 'vitesse': 47}
k=int(input('Veuillez entrer le degré de précision, k= '))



def kppv(): 

    #sortie : liste des k plus proches voisins 
    ecarts=[] #liste avec l ensemble des distances sous forme de tuples (distance,nom,type)
    for pok in charger_data():
        ecarts.append((distance(pok,nouv),pok['nom'],pok["type"]))
    ecarts_triés=sorted(ecarts)

    
    return ecarts_triés[0:k]

print(kppv())

def type_prédit():
   #sortie : le type majoritaire parmi les k plus proches voisins 
    dico={}     # pour chaque type son nombre d'occurence
    for i in kppv():      #on parcourt la liste des plus proches voisins 
        if i[2] in dico.keys() :   
            dico[i[2]]+=1    #on compte le nombre d'occurence de chaque type dans cette liste
        else :
            dico[i[2]]=1    # si le type n'a pas encore été rencontré on l'initialise à 1
    m=(0,0)
    
    for j in dico.keys():
        m=max((dico[j],j),m)    #on identifie le maximum
    return m

print("En comparant au ",k,"plus proches voisins, l'Hippodocus est de type ",type_prédit()[1])

'''une connaissance développée des pokemons permet de savoir que Hippodocus est de type sol
On augmente k jusqu'à obtenir du sol'''