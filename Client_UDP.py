# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Socket Programming: Client_UDP

import socket
server_name = "localhost"
server_port = 2025

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input("Enter a message: ")
    request = msg.encode()
    sock.sendto(request, (server_name, server_port))
    response, server_address = sock.recvfrom(1024)
    print("From server: ", response.decode())
    if msg.lower() == "close":
        print("Client Closed")
        break

sock.close()    