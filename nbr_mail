#!/usr/bin/env python
#coding:utf-8
from email.MIMEText import MIMEText
from email import message_from_string
from email.Message import Message
import poplib

serveur_pop=pop.lib.POP3("pop.domain.com")
serveur_pop.user("febel")
serveur_pop.pass_("python")
nb,taille=serveur_pop.stat()
print "Nombre de mails = ",nb
print "\nTaille totale = ",taille

for i in range(nb):
	print '------------------------'
	print "Message URGENT"
	print '------------------------'
	message=serveur_pop.ret(i+1)
	mail_inline=""
	for ligne in message[1]:
		mail_inline=mail_inline+info+"\n"
	mon_obj_message=message_from_string(mail_inline)
	print mon_onj_message.get('From')
