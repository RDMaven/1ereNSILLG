from socket import socket, AF_INET, SOCK_STREAM


msg = b"bonjour serveur"
hote = 'localhost'
port = 50000

socket_client = socket(AF_INET,SOCK_STREAM)
socket_client.connect((hote,port))
print("Connection serv")
socket_client.send(msg)
print("Fermeture de la connexion")
socket_client.close()
