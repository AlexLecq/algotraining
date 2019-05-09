#Entrainement à l'épreuve Algo BTS SIO

number_enter = ""
number_vol = 0
trig = False


while(type(number_enter) is not int):
	try:
		number_enter = int(input("Veuillez saisir un nombre entier positif : "))
		if(number_enter < 0):
			number_enter = ""
	except ValueError:
		print("Ceci n'est pas un entier positif")

for i in range(1,20):
	if(number_enter % 2 == 0):
		number_enter /= 2
	else:
		number_enter = (number_enter * 3) + 1

	print(number_enter)
	if(number_enter != 1 and trig == False):
		number_vol += 1
	else:
		trig = True
		continue

print("Dernier nombre = " + str(number_enter))
print("Temps de vol = " + str(number_vol))


