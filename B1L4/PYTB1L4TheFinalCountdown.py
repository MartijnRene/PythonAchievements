maxnumber = input("Van hoe hoog wil je aftellen? ")
try:
	if int(maxnumber) > 1:
		for number in range (int(maxnumber), 0, -1):
			print(number)
			if number == 1:
				print("0")
				print("\n*Fart sound*")
	else:
		print("Dat is geen nummer hoger dan 1!")
except ValueError:
	print("Dat is geen nummer!")