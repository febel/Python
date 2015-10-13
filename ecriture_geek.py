#!/usr/local/bin/python3
#--*-- coding:utf8 --*--
Dic={"A":"4","B":"8","C":"(","D":"d","E":"3","F":"f","G":"6","H":"#","I":"1","J":"j","K":"k","L":"1","M":"m","N":"n","O":"0","P":"p","Q":"q","R":"2","S":"5","T":"7","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
msg1=input("entrez votre phrase\n")
msg=msg1.upper()
cpt=0
while cpt<len(msg):
        for cle,valeur in Dic.items():
                if cle==msg[cpt]:
                        print(valeur,end="")
                elif msg[cpt]==" ":
                        print(" ",end="")
                        break
        cpt=cpt+1
print("\n")
