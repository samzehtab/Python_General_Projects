# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Socket Programming: Server_UDP

import socket
server_name = "localhost"
server_port = 2025

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sock.bind((server_name, server_port))

print("The server is ready to recieve client's request.")

while True:
    request, client_address = sock.recvfrom(1024)
    request = request.decode()
    sock.sendto(request.capitalize().encode(), client_address)
    if request.lower() == "close":
        print("Server Closed")
        break

sock.close()
