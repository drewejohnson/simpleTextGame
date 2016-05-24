#-----------
# Andrew Johnson
#
# Simple Text based Game
#-----------

#------------
# Imports
#------------
#Import roomMod as RM
"""
Creation of various game objects and creatures
"""

class GameCharacter:
	className = ""
	desc = ""
	objects = {}
	location = []

	def __init__(self,name,locX,locY):
		self.name = name
		GameCharacter.objects[self.name] = self
		# self.name stores keys as character names, not classNames

	def getDesc(self):
		return "Class: "+self.className+"\n"+self.desc

class Goblin(GameCharacter):
	def __init__(self,name,locX,locY):
		self.className = "goblin"
		self.health = 3
		super().__init__(name,locX,locY)
		self._desc = "A foul goblin called "+self.name.capitalize()

	@property
	def desc(self):	# function for modifying the health line
		healthLine = "Health: {}".format(self.health)
		if self.health >= 3:
			statusLine = "Full strength."
		elif self.health == 2:
			statusLine = "It has a wound on its knee."
		elif self.health == 1:
			statusLine = "Its left arm has been cut off!"
		elif self.health <= 0:
			statusLine = "It is dead."
		return self._desc+"\n"+healthLine+"\n"+statusLine

	@desc.setter
	def desc(self,value):
		self._desc = value

class Player(GameCharacter):
	arms = {}
	legs = {}
	head = {}
	pack = {}
# Items for hands, legs, head, and backpack
#	location = [3,1]
# Assume game space is a 5x5 grid. Start at center edge (5,0)

	def __init__(self,name,locX,locY):
		self.className = "Adventurer"
		self.health = 5
		super().__init__(name,locX,locY)
		self._desc = "A brave adventurer named "+self.name.capitalize()


	@property
	def desc(self):
		"""Returns a string with the inventory of the player"""
# Maybe put the parsing through dictionaries into a class method at some point
		inventory = "Inventory:\n"
		inventory += "Arms: "
		if(len(self.arms)==0):
			inventory +="Nothing\n"
		else:
			for item in self.arms:
				inventory += "{0} {1}\n".format(self.arms[item].itemName,\
					self.arms[item].itemType)
		inventory += "Legs: "
		if(len(self.legs)==0):
			inventory +="Nothing\n"
		else:
			for item in self.legs:
				inventory += "{0} {1}\n".format(self.legs[item].itemName,\
					self.legs[item].itemType)
		inventory += "Head: "
		if(len(self.head)==0):
			inventory +="Nothing\n"
		else:
			for item in self.head:
				inventory += "{0} {1}\n".format(self.head[item].itemName,\
					self.head[item].itemType)
		inventory += "Pack: "
		if(len(self.pack)==0):
			inventory += "Nothing\n"
		else:
			for item in self.pack:
				inventory += "{0} {1}\n".format(self.pack[item].itemName,\
					self.pack[item].itemType)
		return self._desc+"\n"+inventory.rstrip()

	@desc.setter
	def desc(self,value):
			self._desc = value
