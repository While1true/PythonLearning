#encoding:utf_8
import socket as s
from  time import ctime as t

HOST='localhost'
PORT=12455
BUFFER_SIZE=1024
ADDR=(HOST,PORT)
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(ADDR)
while True:
    data=input("> ")
    print(data)
    client.send(b'a1222')
    result=client.recv(BUFFER_SIZE)
    print(str(result))



