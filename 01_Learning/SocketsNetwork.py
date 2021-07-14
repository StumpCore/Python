#Socket is just the endpoint of the communication (endpoint of Network) Server --- client, 2 Sockets
import socket

#tcp for sensible data, slower
#udp, risk of lsoing data, faster

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_DGRAM for udp
s.bind(("127.0.0.1", 55555)) #HOST the socket runs on
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}.".format(address))
    client.send("You are connected".encode())
    client.close()
