from socket import socket, AF_INET, SOCK_STREAM

lclients = []
rep = "n"

def connexion (client, idClient):
    adresseIP = idClient[0]
    port = str(idClient[1])
    print(f"connexion à {adresseIP}:{port}")
    message = ""
    while message.lower() != "finc":
        message = client.recv(50).decode("utf-8")
        print(f"{adresseIP}> {message}")
        client.send((input("You > ")).encode("utf-8"))
    print(f"fermeture de {adresseIP}:{port}")
    client.close()

serveur = socket(AF_INET, SOCK_STREAM)
serveur.bind(('172.20.10.3', 50002))    
serveur.listen(2)
while rep.lower() != "o":
    client, idClient = serveur.accept()
    connexion(client, idClient)
    rep = input("voulez-vous fermer le serveur o/n ? ")
print("fermeture du serveur")
serveur.close()