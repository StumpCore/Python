import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_DGRAM for udp
s.connect(("127.0.0.1", 55555))

message = s.recv(1024)
s.close()
print(message.decode())
