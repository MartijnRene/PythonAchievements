weekdag = input("Welke dag van de week is het? ")
if weekdag == "maandag" or weekdag == "woensdag":
	print("Pak je spullen en ga naar school!")
elif weekdag == "dinsdag" or weekdag == "donderdag" or weekdag == "vrijdag":
	print("Lekker thuis werken!")
elif weekdag == "zaterdag" or weekdag == "zondag":
	print("Het is weekend! Je hebt geen school.")
else:
	print("Dat is geen dag!")