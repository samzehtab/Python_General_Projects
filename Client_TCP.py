# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Socket Programming: Client_TCP

import socket

sock = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM)

sock.connect(("localhost", 2025))

while True:
    data = input("Enter your data: ")
    if data.lower() == "close client": break
    data = data.encode()
    sock.send(data)

print("Goodbye Client!")
sock.close()
