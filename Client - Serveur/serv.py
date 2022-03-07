from socket import socket, AF_INET, SOCK_STREAM

msg = "Oui, c'est moi."
MySocks = socket(AF_INET, SOCK_STREAM)
MySocks.bind(('localhost', 50000))
MySocks.listen(3)
