from socket import socket, AF_INET, SOCK_STREAM
import re #reg ex to get the int in a string.


msg = ""
hote = 'localhost'
port = int(open("./Client - Serveur/port.txt").read())

socket_client = socket(AF_INET,SOCK_STREAM)
socket_client.connect((hote,port))

#Message : You have joined the room.
first_msg = socket_client.recv(200).decode()
print(first_msg)
nb_c = int(re.search(r'\d+', first_msg).group())
if nb_c != 1:
    #Wait for the other user's message.
    print(socket_client.recv(200).decode())


while msg.lower != "finc":
    msg = input("Me > ")
    socket_client.send(msg.encode())
    print(socket_client.recv(200).decode())
print("Fermeture de la connexion")
socket_client.close()
exit()


