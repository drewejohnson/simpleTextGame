#-----------
# Andrew Johnson
# 20 May 2016
#
# Simple Text based Game
#-----------

"""
Creation of various game objects and creatures
"""

class GameCharacter:
	className = ""
	desc = ""
	objects = {}

	def __init__(self,name):
		self.name = name
		GameCharacter.objects[self.name] = self
		# self.name stores keys as character names, not classNames

	def getDesc(self):
		return "Class: "+self.className+"\n"+self.desc

class Goblin(GameCharacter):
	def __init__(self,name):
		self.className = "goblin"
		self.health = 3
		super().__init__(name)
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
	hands = {}
	legs = {}
	head = {}
	pack = {}

	def __init__(self,name):
		self.className = "Adventurer"
		self.health = 5
		super().__init__(name)
		self.desc = "A brave adventurer named "+self.name.capitalize()
# Items for hands, legs, head, and backpack


	def packUpdate(self,itemName):
		Adventurer.pack[self.itemName] = self
