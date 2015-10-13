#!/usr/local/bin/python3
#--*--coding:utf8--*--
import socket,sys 
host=sys.argv[1] 
textport=sys.argv[2] 
fichier=sys.argv[3]
try: 
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
except socket.error as e: 
        print("erreur lors de la création du socket : ",e)  
        sys.exit(1) 
try: 
        port=int(textport) 
except ValueError: 
        try: 
                port=socket.getservbyname(host,'tcp') 
        except socket.error as e: 
                print("ne trouve pas le port ",e)  
                sys.exit(1) 
try: 
        s.connect((host,port)) 
except socket.gaierror as e: 
        print("erreur d'adresse de connexion au serveur : ",e)  
        sys.exit(1) 
except socket.error as e: 
        print("erreur de connexion: ",e)  
        sys.exit(1) 
try: 
        s.sendall(bytes("GET %s HTTP/1.0\r\n\r\n"%fichier,'UTF-8')) 
except socket.error as e: 
        print("erreur d'envoi des données : ",e)  
        sys.exit(1) 
while 1: 
        try: 
                buf=s.recv(2048) 
        except socket.error as e: 
                print("erreur de reception des données: ",e)  
                sys.exit(1) 
        if not len(buf): 
                break 
        print(buf)
