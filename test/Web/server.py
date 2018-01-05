#encoding:utf_8
import socket as s
from  time import ctime as t
import re
import threading as th
HOST=''
PORT=1111
BUFFER_SIZE=1024
ADDR=(HOST,PORT)


rex=r'\d+\:\d+\:\d+'
def whileloop(sock):
    while (True):
        recv = sock.recv(BUFFER_SIZE)
        if not recv:
            break
        print(">>>>get message from %s : %s" % (addr, recv))
        sock.send(bytes(('Server:get your message :%s, TKS' % recv).encode("utf-8")))
server=s.socket(s.AF_INET,s.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
while(True):
    print("waiting for client to connecting...")
    sock,addr = server.accept()
    print(">>>%s connected currentTime:%s" % (addr,re.search(rex,t()).group()))
    tt=th.Thread(whileloop(sock))
    tt.start()
    tt.join()

