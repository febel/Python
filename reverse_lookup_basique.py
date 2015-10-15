#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
import sys, socket

try:
    result=socket.gethostbyaddr(sys.argv[1])
    print "le nom d'hôte primaire est :"
    print " "+result[0]
    
    print "\nAdresse :"
    for item in result[2]:
        print " "+item
        
except socket.herror, e:
    print "ne peux resoudre :", e
