#!/usr/bin/env python3
#--*--coding:utf8--*--

import os,sys

Ip=input("Veuillez entrer une adresse ip\n")
try:
	IPl=Ip.split('.')
	for i in IPl:
		int(i)
except:
	print("ce n'est pas une adresse ip")
	sys.exit()
IPl.pop()
IPf=".".join(IPl)
for i in range(1,255):
	IPv=IPf +"."+str(i)
	print(IPv)	
	resu=os.system("ping -c 1 -W 1 " + IPv+" >/dev/null")
	if resu == 0:
		print("l'adresse %s repond"%IPv)
	else:
		print("l'adresse %s ne repond pas"%IPv)
