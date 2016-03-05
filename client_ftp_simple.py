#!/usr/local/bin/python3
#--*--coding:utf8--*--
import socket

host=""
port=21
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) ; création de l’objet socket
s.connect((host,port)) ; connexion au FTP via la méthode connect()
data=s.recv(1204) ; lecture de la bannière
print data
s.send("USER anonymous\r\n") ; envoie du login
data=s.recv(1024) ; réception de la réponse
print data
s.send("PASS test@free.fr\r\n") ; envoie du mot de passe
data=recv(1024) ; réception de la réponse
print data
s.send("QUIT\r\n") ; nous quittons le FTP
s.close()
