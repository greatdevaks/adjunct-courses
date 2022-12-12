# Example: Server Socket Program.

import socket

HOST = ""  # Denotes that the socket is available to bind on all available interfaces.
PORT = 50008  # Arbitrary non-privileged port on which the Server should be accepting the connections. Non-privileged ports are > 1023.
with socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
) as s:  # socket.socket() supports Context Manager type.
    s.bind((HOST, PORT))
    s.listen(1)
    (
        conn,
        addr,
    ) = (
        s.accept()
    )  # Returns a new socket object, representing the connection and holding the address of the client.
    with conn:
        print(f"Connected by: {addr}")
        while True:
            data = conn.recv(1024)  # Reads the data sent by the client.
            if not data:
                break
            conn.sendall(data)  # Echoes the data.
