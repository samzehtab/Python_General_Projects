# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Socket Programming: Server_TCP

import socket

sock = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM)

sock.bind(("localhost", 2025))

sock.listen()

connection, client = sock.accept()

# Debugging
print(f"{client} connected")

while True:
    data = connection.recv(32)
    data = data.decode()
    if data.lower() == "close server": break
    print("Recieved Data: ", data)
    
print("Goodbye Server!")
connection.close()
