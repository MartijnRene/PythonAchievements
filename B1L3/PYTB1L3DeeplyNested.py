if hungry:
	if !cookmood:
		if !leftovers:
			if !money:
				goCook()
			else:
				orderPizza()
		else:
			eatLeftovers()
	else:
		goCook()
else:
	eatNothing()