#!/usr/local/bin/python3
#--*--coding:utf8--*--
import urllib.request


response = urllib.request.urlopen("http://www.wsbtv.com/s/weather/")
html = response.read()
text = str(html)		#conversion des octets en chaine de caractére.

#recherche du signe °
endOfTemp = text.find("&deg;")

index = endOfTemp
ch = text[index]

while ch != ">":
    index = index - 1
    ch = text[index]

startOfTemp = index  + 1

textTemp = text[startOfTemp:endOfTemp]
tempInt = (int(textTemp)-32)/1.8
print( "la temperature est de :%i C°"%tempInt)
