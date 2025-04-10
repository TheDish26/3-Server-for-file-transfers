# 3-Server-for-file-transfers
A simple socket-based server-client application for transferring files between a local machine and a remote server.
# Server for File Transfers

This project is a basic server application for handling file transfers between a client and a server. It allows you to upload and download files from the server using simple socket programming.

---

## 📌 Prerequisites

Make sure the following are installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)

---

## 🚀 Project Setup

### 1. **Clone the Repository**

Open your terminal and run:

```bash
git clone https://github.com/TheDish26/file-transfer-server.git
cd file-transfer-server

import socket
import os

# Set up server address and port
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 65432        # Port to listen on

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Start listening for incoming connections
server_socket.listen()

print(f"Server started at {SERVER_HOST}:{SERVER_PORT}. Waiting for a connection...")

# Accept incoming connection from client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive the file name from the client
file_name = client_socket.recv(1024).decode()
print(f"Receiving file: {file_name}")

# Open the file to write data received from the client
with open(f"received_{file_name}", 'wb') as file:
    while True:
        # Receive data in chunks
        file_data = client_socket.recv(1024)
        if not file_data:
            break
        file.write(file_data)

print("File transfer complete!")

# Close the client and server sockets
client_socket.close()
server_socket.close()
