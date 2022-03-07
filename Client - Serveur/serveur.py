from socket import socket, AF_INET, SOCK_STREAM

msg = """HTTP/1.1 200 OK
Content-Type: text/html \n
<!doctype html>
<html>
<div style="background-color: pink; height : 300px; width: 300px; margin:auto">
<h1 style="color:red; margin:auto; height:100px; width:100px; align : center;">MAAA LA PIZZA</h1>
<img src="https://www.pngmart.com/files/1/Pepperoni-Pizza-PNG-Transparent-Image.png" style="height: 300px;margin:auto;">
</div>
</html>"""
MySocks = socket(AF_INET, SOCK_STREAM)
MySocks.bind(('172.20.10.3', 50003))
MySocks.listen(1)
connect = True

while connect:
    client, addresse = MySocks.accept()
    reponse = client.recv(50)
    print(f"Client {addresse} connecté.\n  : {reponse}")

    client.send(msg.encode())
    client.close()
    connect = False

print('Fermeture du serv.')
MySocks.close()