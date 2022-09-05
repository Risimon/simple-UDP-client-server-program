import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))

while True:
    clientsocket, bytesAddressPair = s.recvfrom(1024)
    print(f"Connection from {bytesAddressPair[1]} has been establieshed!")
    clientsocket.sendto(bytes("Wlcome to the server!", bytesAddressPair[1]))
    
