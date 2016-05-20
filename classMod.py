#-----------
# Andrew Johnson
# 19 May 2016
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
		GameObject.objects[self.className] = self

	def getDesc(self):
		return self.className+"\n"+self.desc

class Goblin(GameCharacter):
	def __init__(self,name):
		self.className = "goblin"
		self.health = 3
		super().__init__(name)
		self._desc = "A foul creature called "+self.name

	@property
	def desc(self):	# function for modifying the health line
		if self.health >= 3:
			return self._desc
		elif self.health == 2:
			healthLine = "It has a wound on its knee."
		elif self.health == 1:
			healthLine = "Its left arm has been cut off!"
		elif self.health <= 0:
			healthLine = "It is dead."
		return self._desc+"\n"+healthLine

	@desc.setter
	def desc(self,value):
		self._desc = value

class Adventurer(GameObject):
	def __init__(self,name):
		self.className = "Adventurer"
		self.health = 5
		super().__init__(name)
		self._desc = "A brave adventurer named"+self.name
# Items for hands, legs, head, and backpack
		self.hands = []
		self.legs = []
		self.head = []
		self.pack = []
