import socket

server = socket.socket()

server.bind(("127.0.0.1", 5555))
server.listen(1)

print("Server waiting for connection...")

client, addr = server.accept()
print("Connected to:", addr)

filename = input("Enter file name to send: ")

with open(filename, "rb") as file:
    data = file.read()
    client.send(data)

print("File sent successfully")

client.close()
server.close()
