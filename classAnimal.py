from AnimalFile import *
import random
names = ("Lolo", "Piggy", "Moly", "Nemo", "Tehila") 
sounds= ("mfff", "bzzzz", "grrrr", "hihihih", "wooof", "mooooo")
ages = (10, 50, 9, 15, 7, 14, 5)
foods = ("Apple", "Pizza", "Cookies", "Hamburger", "pear", "Bread")
dreams = ("Unicorns", "Food", "Rain", "Disney Land")
#dog = Animal("woof", "Jeff", 17)
#cat = Animal("meow", "Lolo", 4)
#bee = Animal("bzzz", "Cookie", 9)

#print(dog.sound)

#dog.eat("Bamba")
#cat.eat("Bisley")
#cat.sleep("Unicorns")
for i in range(0, 30):	
	dog = Animal(sounds[random.randint(0,5)], names[random.randint(0, 4)], ages[random.randint(0,6)])
	dog.sleep(dreams[random.randint(0,3)])
for g in range(0, 50):
	cat = Animal(sounds[random.randint(0,5)], names[random.randint(0, 4)], ages[random.randint(0,6)])
	cat.eat(foods[random.randint(0,5)])
for t in range(0, 220):
	bee = Animal(sounds[random.randint(0,5)], names[random.randint(0, 4)], ages[random.randint(0,6)])
