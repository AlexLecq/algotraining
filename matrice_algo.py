#Entrainement algoritheme BTS SIO

from random import *


def contraste(matrice, luminosite):
	for i in range(0, len(matrice)):
		for j in range(len(matrice[0])):
			if(matrice[i][j] < luminosite):
				matrice[i][j] /= 2
			else:
				matrice[i][j] *= 2
				if matrice[i][j] > 100 :
					matrice[i][j] = 100
	return matrice

def luminosite(matrice):
	sum = 0
	n = 0
	for i in range(0,len(matrice)):
		for j in range(0, len(matrice[0])):
			sum += matrice[i][j]
			n += 1
	return sum / n


def ecrire_matrice(matrice):
	for i in range(0,len(matrice)):
		for j in range(0, len(matrice[0])):
			print(matrice[i][j] , end=' ')
		print()


def gen_matrice():
	l = randint(1,5)
	c = randint(1,5)
	matrice = [[0] * c for i in range(0,l)]
	for i in range(0, l) :
		for j in range(0, c):
			matrice[i][j] = randrange(0 , 100 , 25)
	return matrice




matrice = gen_matrice()
print('La matrice est la suivante : \n ')
ecrire_matrice(matrice)
m = luminosite(matrice)
print('Sa luminosité est de ' + str(m) + '\n ')
print('Voici la matrice après l\'ajustement de contraste : ')
ecrire_matrice(contraste(matrice , m))



