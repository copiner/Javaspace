
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 3366))

print(s.recv(1024).decode('utf-8'))
for data in [b'Duncan', b'Manu', b'Parker']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    print('francis')
s.send(b'exit')
s.close()
