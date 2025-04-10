import socket
import os

# Set up server address and port
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 65432        # Same port as the server

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# File to send to the server
file_name = 'example_file.txt'

# Send the file name to the server
client_socket.send(file_name.encode())

# Open the file to send
with open(file_name, 'rb') as file:
    while chunk := file.read(1024):
        # Send data in chunks to the server
        client_socket.send(chunk)

print("File transfer complete!")

# Close the client socket
client_socket.close()
server_socket.close()  # Close the server socket as well
