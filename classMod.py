#-----------
# Andrew Johnson
#
# Simple Text based Game
#-----------
"""Creation of various game objects and creatures"""
#------------
# Imports
#------------
import roomMod as RM


class GameCharacter:
	className = ""
	desc = ""
	objects = {}

	def __init__(self,name,sweep):#,locX,locY):
		self.name = name
		GameCharacter.objects[self.name] = self
		RM.addToRoom(name,sweep)
		# self.name stores keys as character names, not classNames

	def getDesc(self):
		return "Class: "+self.className+"\n"+self.desc

class Goblin(GameCharacter):
	def __init__(self,name,sweep):#,locX,locY):
		self.className = "goblin"
		self.health = 3
		super().__init__(name,sweep)#,locX,locY)
		self._desc = "A foul goblin called "+self.name.capitalize()

	@property
	def desc(self):	
		healthLine = "Health: {}".format(self.health)
		return self._desc+"\n"+healthLine#+statusLine

	@desc.setter
	def desc(self,value):
		self._desc = value

class Player(GameCharacter):
	arms = {}
	legs = {}
	head = {}
	pack = {}
	pos = {}
# Items for hands, legs, head, and backpack
#	location = [3,1]
# Assume game space is a 5x5 grid. Start at center edge (5,0)

	def __init__(self,name,sweep):#,locX,locY):
		self.className = "Adventurer"
		self.health = 5
		super().__init__(name,sweep)#,locX,locY)
		self.pos[sweep] = RM.rooms[sweep]
		self._desc = "A brave adventurer named "+self.name.capitalize()


	@property
	def desc(self):
		"""Returns a string with the inventory of the player"""
# Maybe put the parsing through dictionaries into a class method at some point
		inventory = "Inventory:\n"
		if(len(self.arms)==0):
			inventory += "Arms: Nothing\n"
		else:
			inventory += "Arms: \n"
			for item in self.arms:
				inventory += "  {0} {1}\n".format(self.arms[item].itemName,\
					self.arms[item].itemType)
		if(len(self.legs)==0):
			inventory +="Legs: Nothing\n"
		else:
			inventory += 'Legs: \n'
			for item in self.legs:
				inventory += "  {0} {1}\n".format(self.legs[item].itemName,\
					self.legs[item].itemType)
		if(len(self.head)==0):
			inventory +="Head: Nothing\n"
		else:
			inventory += "Head: \n"
			for item in self.head:
				inventory += "{0} {1}\n".format(self.head[item].itemName,\
					self.head[item].itemType)
		if(len(self.pack)==0):
			inventory += "Pack: Nothing\n"
		else:
			inventory += "Pack: \n"
			for item in self.pack:
				inventory += "{0} {1}\n".format(self.pack[item].itemName,\
					self.pack[item].itemType)
		return self._desc+'\nHealth: '+str(self.health)+"\n"+inventory.rstrip()

	@desc.setter
	def desc(self,value):
		self._desc = value

#----------
# Functions
#----------

def getLoc():
	"""Returns the location of the player"""
	return list(Player.pos.keys())[0]
