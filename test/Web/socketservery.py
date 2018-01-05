#encoding:utf_8
from SocketServer import *
from  time import ctime as t
import re
import threading as th
HOST='localhost'
PORT=12455
BUFFER_SIZE=1024
ADDR=(HOST,PORT)
class Myh(StreamRequestHandler):
    def handle(self):
        print('>>>client coming: ',self.client_address)
        print(self.rfile.readline())


        print('end')

tcpService=TCPServer(ADDR,Myh)

print('waiting for connecting....')
tcpService.serve_forever()