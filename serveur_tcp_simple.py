#!/usr/bin/env python  
#--*-- coding:UTF-8 --*--  
 
import socket  
 
host=''  
port = 1338  
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.bind((host,port))  
s.listen(1)  
client,adresse=s.accept()  
print adresse  
print client.getpeername()  
client.send("Bonjour Editions ENI\n entrez un mot ou fin si vous 
voulez arreter la discussion ")  
while 1:  
        data=client.recv(1024)  
        if data=="fin\n":  
                break  
        print "Client > " + data  
        mot=raw_input("Serveur > ")  
        client.send(mot)  
client.close()  
s.close() 
