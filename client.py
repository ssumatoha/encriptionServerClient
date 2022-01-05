import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

a = random.randint(1, 1000)

p, g = 7, 5
A = g ** a % p
sock.send(pickle.dumps((g, p, A)))

data = sock.recv(1024)
B = pickle.loads(data)

K = B ** a % p
print(K)

sock.close()
