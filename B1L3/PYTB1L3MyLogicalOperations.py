name = "erwin henraat"
job = "teacher"
moneyInAccount = 1300

#Vervang de ** met de logische operatoren 'and' en/of 'or'

#Zorg dat de if statement de functie buyABrandNewMotorcycle uitvoert als:
# Mijn naam erwin henraat is en ik een baan heb.
# Of als ik meer dan 10000 euro op mijn rekening heb staan.

def buyABrandNewMotorcycle():
    for index in range(100):
        print(":)")

if name == "erwin henraat" and job != None or moneyInAccount > 10000:
    buyABrandNewMotorcycle()

#Maak nu voor jezelf ook een logische voorwaarde waarin je de operatoren 'and' en 'or' gebruikt.
name = "martijn van der meer"
job = "snackbarmedewerker"
stufi = True

if name == "martijn van der meer" and job != None or stufi == True:
	print("Je krijgt iedere maand geld!")