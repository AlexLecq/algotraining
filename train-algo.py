#Entrainement algorithme appliqué

number_enter = 1
i = 0

while(i < 8):
	if(number_enter % 2 == 0):
		number_enter += 1
	else:
		number_enter = (number_enter + i) * 2
	i += 1
	print(number_enter)



