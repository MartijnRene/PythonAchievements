print("Your alarm rings. Do you WAKE UP or SNOOZE?")
choice = input()
if choice == "WAKE UP":
	print("You get out of bed but still feel tired. If only you could've slept 5 more minutes.")
elif choice == "SNOOZE":
	print("You snooze for what feels like 5 more minutes but wake up 30 minutes later instead. You're late!")
else:
	print(choice, "wasn't a valid choice")

print("You go downstairs to eat breakfast. Do you eat CEREAL or BREAD?")
choice = input()
if choice == "CEREAL":
	print("You pour some cereal and milk into a bowl, in that order. As it should be.")
elif choice == "BREAD":
	print("You butter some bread and put some spread on it, ready to go!")
else:
	print(choice, "wasn't a valid choice")

print("Do you take PUBLIC transport or do you go by CAR?")
choice = input()
if choice == "PUBLIC":
	print("You put on your facemask and check in on the bus. Now you can relax for a bit while you travel to school.")
elif choice == "CAR":
	print("You get in your car and drive through the traffic.")
else:
	print(choice, "wasn't a valid choice")

print("You arrive at school. Do you go straight to CLASS or do you HANG with your friends for a bit?")
choice = input()
if choice == "CLASS":
	print("You arrive at the class and you're the first one there. You take a seat at the back and wait for class to start.")
elif choice == "HANG":
	print("You hang with your friends for a bit and are almost late to class!")
else:
	print(choice, "wasn't a valid choice")

print("Class ends and it's a lunch break. Do you eat at SCHOOL or do you go to the BURGER KING?")
choice = input()
if choice == "SCHOOL":
	print("You eat the sandwich you made and wait for class to start again.")
elif choice == "BURGER KING":
	print("You go to the nearby Burger King and grab a burger. Much tastier than regular bread!")
else:
	print(choice, "wasn't a valid choice")