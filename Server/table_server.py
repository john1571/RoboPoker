import socket
import selectors
import traceback
import sys

import Server.libserver as libserver

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept() # should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)

def run_server():
    host, port = sys.argv[]

def table_server():
    # set hostname

    # check for available socket
        # check for connections
    # deal


    # get the hostname
    host = socket.gethostname()
    port = 5050  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    conn2, address2 = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address2))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        conn.send("waiting on other user".encode())  # send data to the client
        if not data:
            # if data is not received break
            break
        if data:
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client
        data2 = conn2.recv(1024).decode()
        if not data2:
           break
        if data2:
            print("from connected user: " + str(data2))
            data2 = input(' -> ')
            conn2.send(data2.encode())  # send data to the client
    conn.close()  # close the connection
    conn2.close()


if __name__ == '__main__':
    server_program()