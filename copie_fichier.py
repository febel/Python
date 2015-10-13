source = open("fichier1.txt","r")
destination = open("lacopie.txt","w")
for ligne in source:
	destination.write(ligne)
destination.close()
source.close()

source=open("fichier1.txt","r")
destination=open("fichier3.txt","w")
destination.write(source.read())
destination.close()
source.close()


source = open("fichier1.txt","r")
destination = open("lacopie2.txt","w")
while True:
	data=source.read(5)
	if data=="":
		break
	destination.write(data)
destination.close()
source.close()
