# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Socket Programming: Client_HTTP

import socket
IP = "dolenz.ir"
PORT = 80
socket_address = (IP, PORT)

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

sock.connect(socket_address)

cmd = "GET https://dolenz.ir/wp-content/uploads/2024/08/Bald_eagle_about_to_fly_in_Alaska_2016-1024x819.jpg HTTP/1.0\r\n\r\n"
cmd = cmd.encode()

sock.sendall(cmd)

picture = b""
with sock:
    while True:
        data = sock.recv(1024)
        if len(data) < 1: break
        picture += data

pos = picture.find(b"\r\n\r\n")
print(picture[:pos])

with open(r"C:\Users\User\Desktop\Advanced Python\Exercises\test.jpg", "wb") as fh:
    fh.write(picture[pos + 4:])