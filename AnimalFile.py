class Animal(object):
	def __init__(self, sound, name, age):
		self.sound = sound
		self.name = name
		self.age = age
	def eat(self, food):
		print(self.name + " is eating " + food)
	def sleep(self, dream):
		print(str(self.age) +" yeara old "+ self.name + " is dreaming of "+ dream) 

