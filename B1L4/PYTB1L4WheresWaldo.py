import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
stoel = people.index("Waldo")

print(people)
print("Waldo zit op stoel nummer", stoel + 1)
#Er is geen stoel nummer 0