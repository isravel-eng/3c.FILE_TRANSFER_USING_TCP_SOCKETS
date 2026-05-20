import socket

client = socket.socket()

client.connect(("127.0.0.1", 5555))

save_name = input("Enter name to save file: ")

data = client.recv(1000000)

with open(save_name, "wb") as file:
    file.write(data)

print("File received successfully")

client.close()
