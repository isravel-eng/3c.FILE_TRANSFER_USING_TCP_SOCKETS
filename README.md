# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS

## AIM
To write a python program for creating File Transfer using TCP Socket Links.

## ALGORITHM
1. Import the necessary python modules.
2. Create a socket connection using socket module.
3. Bind the server with IP address and port number.
4. Open the file and send it to the client in byte format.
5. In the client side receive the file from server.
6. Write the received content into a new file.
7. Close the socket connection.

## PROGRAM

### fileserver.py
```python
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
```

### fileclient.py
```python
import socket

client = socket.socket()

client.connect(("127.0.0.1", 5555))

save_name = input("Enter name to save file: ")

data = client.recv(1000000)

with open(save_name, "wb") as file:
    file.write(data)

print("File received successfully")

client.close()
```

## OUTPUT

### Server Side
```text
Server waiting for connection...
Connected to: ('127.0.0.1', 54321)
Enter file name to send: sample.txt
File sent successfully
```
<img width="599" height="109" alt="image" src="https://github.com/user-attachments/assets/fe553292-6045-4fbf-95c2-3270d1a936a4" />

### Client Side
```text
Enter name to save file: received.txt
File received successfully
```
<img width="579" height="64" alt="image" src="https://github.com/user-attachments/assets/273a9233-4c5f-429b-a524-66e75e171fb9" />

### File Content
```text
Hello Python Socket Programming
```

## RESULT
Thus, the python program for creating File Transfer using TCP Socket Links was successfully created and executed.
