
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Duncan',b'Manu',b'Parker']:

    s.sendto(data, ('127.0.0.1', 3388))

    print(s.recv(1024).decode('utf-8'))

s.close()
