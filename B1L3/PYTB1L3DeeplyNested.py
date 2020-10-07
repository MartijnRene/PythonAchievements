hungry = True
cookmood = False
leftovers = False
money = 210

def goCook():
	print("Ga koken!")
def orderPizza():
	print("Bestel een pizza.")
def eatLeftovers():
	print("Eet nog wat restjes van gisteren.")
def eatNothing():
	print("Als je geen honger hebt hoef je ook niet te eten.")

if hungry:
	if not cookmood:
		if not leftovers:
			if money < 200:
				goCook()
			else:
				orderPizza()
		else:
			eatLeftovers()
	else:
		goCook()
else:
	eatNothing()