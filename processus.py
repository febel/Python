#!/bin/env python3
# -*- coding: utf-8 -*-

import os 
import time 
import sys 

child_pid = os.fork()

if child_pid == 0: # code enfant
	print('enfant: je suis le processus enfant') 
	try:
		print('enfant: je travail') 
		time.sleep(2) 
		print("enfant: j'ai fini")
	except:
		lerr = '%s: %s' % (sys.exc_info()[0], sys.exc_info()[1]) 
		print('Erreur dans le processus enfant:\n %s' % lerr)
else:
	# code parent
	print('pere: je suis le processus pere') 
	print("pere: j'attends le processus enfant") 
	os.wait()
	print('pere: le processus enfant a terminé')
