#Entrainement Algo BTS SIO 

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def codage(message):
	longueur = len(message)
	messageCode = ''
	for i in range(0,longueur):
		rang = find(message[i])
		if rang == -1:
			messageCode += message[i]
		else:
			rangCode = rang + 13
			if rangCode > 25:
				rangCode -= 26

			lettreCode = alphabet[rangCode]
			messageCode += lettreCode

	return messageCode

def find(letter):
	for i in range(0, len(alphabet)) :
		if letter == alphabet[i] :
			return i
		else:
			continue
	return -1


while(True):
	try:
		enter = input('Veuillez saisir un mot pour l\'encodage : ')
		if len(enter) < 10 and enter.isupper():
			break
		else:
			continue
	except ValueError:
		print('Votre mot doit être composé de lettre en majuscule')


print('Votre mot après encodage : ' + codage(enter))
