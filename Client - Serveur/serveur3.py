#===== Libs =====#
import socket
import threading
#================#

#===== INIT =====#
# --- just VAR --- #
lclients = [] # for multithread
connect = True # variable to open/close the connection.
list_d_clients = [] # list of dictionnaries to define the users.
d_client = {} # dictionnary to define a user.
nb_c = 0 # Number of clients
# ---------------- #

# --- HOST --- #
hote = 'localhost' # IP of the host/server.
port = int(open("./Client - Serveur/port.txt").read()) # port of the host/server.
# ------------ #
#================#

#===== VERBOSE OPTION =====#
print()
verbose_ask = input("Verbose y/n : ")
if verbose_ask == "y":
    verbose = True
else : verbose = False
#==========================#

#===== FUNCTIONS =====#
def connexion (client, idClient):
    adresseIP = idClient[0]
    port = str(idClient[1])
    #print("\nConnexion à " + adresseIP + ":" + port)
    Alias_client_dico = {}
    for i in list_d_clients:
        if i['id'] == client:
            Alias_client_dico[adresseIP] = i['alias']
       
    for i in list_d_clients:
            if i['id'] != client:
                i["id"].send((f"{Alias_client_dico} ").encode("utf-8"))

    #=======VERBOSE OPTION=======
    #if verbose == True:
        #print(Alias_client_dico)
        #print(list_d_clients)
    #============================

    message = ""
    while message.lower() != "finc":
        message = client.recv(200).decode("utf-8")
        
        #=======VERBOSE OPTION=======
        if verbose == True:
            resent = f"{Alias_client_dico[adresseIP]} ({adresseIP}:{port}) > {message}"
        #============================
        else: 
            resent = f"{Alias_client_dico[adresseIP]} > {message}"

        print(resent)
        for i in list_d_clients:
            if i['id'] != client:
                i['id'].send((resent).encode("utf-8"))
    print("fermeture de " + adresseIP + ":" + port)
    client.close()
#=====================#

#===== SETUP =====#
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((hote, port))    
serveur.listen(2)
#=================#

#===== MAIN =====#
while connect:
    client, idClient = serveur.accept()
    
    # --- Setup for client --- #
    d_client['id'] = client
    d_client['ip'] = idClient[0]
    d_client['port'] = int(idClient[1])

    print("\n+--------------------------------------------+")
    print(f"Connexion à {d_client['ip']}:{str(d_client['port'])}")
    print("+--------------------------------------------+\n")


    d_client['alias'] = input(f"Alias for {d_client['ip']}:{d_client['port']} : ")


    list_d_clients.append(d_client)

    
    print(d_client)
    print(list_d_clients)

    nb_c = len(list_d_clients)

    # ------------------------ #

    for user in list_d_clients:
        if user['alias'] != d_client['alias']:
            user["id"].send((f"{d_client['alias']} has joined the room. ({nb_c})").encode("utf-8"))
        elif user['alias'] == d_client['alias']:
            user["id"].send((f"You have joined the room. ({nb_c})").encode("utf-8"))

    lclients.append(threading.Thread(target=connexion, args=(client, idClient)))
    lclients[-1].start()
#================#



serveur.close()