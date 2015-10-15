#!/usr/bin/env python
import sys, os, string
ROT13 =string.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ','nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
fichier = open("dictionnaire")
Fichier = fichier.readlines()
for root, dir, files in os.walk(str(sys.argv[1])):
	for file in files:
		if ".txt" in str(file):
			trouvemot = 0
			pasmot = 0
			lignes = open(file).readlines()
			for ligne in lignes:
				traductionligne=ligne.translate(ROT13)
				traductionmots=traductionligne.split()
				for chaquemot in traductionmots:
					if (chaquemot+'\n') in Fichier:
						trouvemot=trouvemot+1
					else:
						pasmot = pasmot+1
			if (trouvemot > pasmot):
				print file+" peut contenir un cryptage ROT-13."
