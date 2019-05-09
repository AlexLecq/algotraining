#Algo afin de pouvoir choisir un algo à partir d'un menu 

from os import *

quit = ''

while quit != 'y':
	while(True):
		try:
			print()
			inp = int(input('1. Algo de la matrice \n2. Algo de la suite Syracuse \n3. Algo de la cryptographie \n'))
			if 1 <= inp <= 3: break
			else: continue
		except ValueError:
			print('Il faut saisir une valeur comprise en 1 et 3 !')


	if inp == 1: system('python matrice_algo.py')
	elif inp == 2: system('python syracuse_algo.py')
	elif inp == 3: system('python crypto_rot13_algo.py')
	print()
	quit = str(input('Voulez vous quitter ? (y/n)'))
