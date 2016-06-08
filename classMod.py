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
import verbFuncMod as VFM
#-------------------
# Classes for Characters
#-------------------
class GameCharacter:
	className = ""
	desc = ""
	objects = {}
	values = []		# health, attack, defense

	def __init__(self,name,sweep,values):#,locX,locY):
		self.name = name
		GameCharacter.objects[self.name] = self
		self.values = values
		RM.addToRoom(name,sweep)
		# self.name stores keys as character names, not classNames

	def getDesc(self):
		return "Class: "+self.className+"\n"+self.desc


	def valEnhance(self,enhanceStr,eMod):
		"""
		enhanceStr: string that governs attribute modification.
		eMod: add (0) or subtract (1) enhancement
		"""
		if len(enhanceStr) % 2 != 0:
			raise SystemExit('String of odd length in valEnhance')
		for c in range(0,len(enhanceStr),2):
			if enhanceStr[c] == 'a':
				self.values[1] += int(enhanceStr[c+1])*(-1)**eMod
				return 0
			elif enhanceStr[c] =='d':
				self.values[2] += int(enhanceStr[c+1])*(-1)**eMod
				return 0
			elif enhanceStr[c] == 'h':
				self.values[0] += int(enhanceStr[c+1])*(-1)**eMod
				return 0
			else:
				raise SystemExit("Bad enhancer in valEnhance")

class Goblin(GameCharacter):
	def __init__(self,name,sweep):#,locX,locY):
		self.className = "goblin"
		gobValues = [5,2,2]			# 5 health, 1 attack and defense
		super().__init__(name,sweep,gobValues)#,locX,locY)
		self._desc = "A foul goblin called "+self.name.capitalize()


	@property
	def desc(self):
		# Return goblin name and health
		return self._desc+"\nHealth: "+str(self.values[0])

	@desc.setter
	def desc(self,value):
		self._desc = value


class Werewolf(GameCharacter):
	def __init__(self,name,sweep):
		self.className = "werewolf"
		wolfValues = [6,4,5]
		super().__init__(name,sweep,wolfValues)
		self._desc = "A ferocious wolf named "+self.name.capitalize()

	@property
	def desc(self):
		return self._desc+"\nHealth: {0}".format(self.values[0])

	@desc.setter
	def desc(self,value):
		self._desc = value


class Elf(GameCharacter):
	def __init__(self,name,sweep):
		self.className = "elf"
		elfValues = [8,3,7]
		super().__init__(name,sweep,elfValues)
		self._desc = "An estranged elf named {}".format(self.name.capitalize())

	@property
	def desc(self):
		return self._desc+"\nHealth: {0}".format(self.values[0])

	@desc.setter
	def desc(self,value):
		self._desc = value


class Wizard(GameCharacter):
	def __init__(self,name,sweep):
		self.className = "wizard"
		wizValues = [10,7,8]
		super().__init__(name,sweep,wizValues)
		self._desc = "A powerful wizard named {}".format(self.name.capitalize())

	@property
	def desc(self):
		return self._desc+"\nHealth: {0}".format(self.values[0])

	@desc.setter
	def desc(self,value):
		self._desc = value


class Dragon(GameCharacter):
	def __init__(self,name,sweep):
		self.className = "dragon"
		dragonValues = [15,15,15]
		super().__init__(name,sweep,dragonValues)
		self._desc = "An enraged, gigantic dragon known as {}".format(self.name.capitalize())

	@property
	def desc(self):
		return self._desc+"\nHealth: {0}".format(self.values[0])

	@desc.setter
	def desc(self,value):
		self._desc = value


class Player(GameCharacter):
	arms = {}
	legs = {}
	head = {}
	pack = {}
	pos = {}

	def __init__(self,name,sweep):#,locX,locY):
		self.className = "Adventurer"
		pValues = [5,2,2]
		super().__init__(name,sweep,pValues)#,locX,locY)
		self.pos[sweep] = RM.rooms[sweep]
		self._desc = "A brave adventurer named "+VFM.pName.capitalize()


	@property
	def desc(self):
		"""Returns a string with the inventory and location of the player"""
# Maybe put the parsing through dictionaries into a class method at some point
		stats = "Health: {0:3d} Attack: {1:3d} Defense: {2:3d}\n".\
			format(self.values[0],self.values[1],self.values[2])
		location = "Location: ({0},{1})\n".\
			format(RM.sweepFunc(getLoc())[0],RM.sweepFunc(getLoc())[1])
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
				inventory += "  {0} {1}\n".format(self.head[item].itemName,\
					self.head[item].itemType)
		if(len(self.pack)==0):
			inventory += "Pack: Nothing\n"
		else:
			inventory += "Pack: \n"
			for item in self.pack:
				inventory += "  {0} {1}\n".format(self.pack[item].itemName,\
					self.pack[item].itemType)
		return self._desc+"\n"+stats+location+inventory.rstrip()


	@desc.setter
	def desc(self,value):
		self._desc = value

#----------
# Functions
#----------

def getLoc():
	"""Returns the sweep of the player"""
	pList = list(Player.pos.keys())
	if len(pList) > 1:
		raise SystemExit('Player in multiple places at once - getLoc')
	else:
		return pList[0]
#-----------
# Enemy Names
#------------

gobNames = ["Gob1","Gob2","Gob3","Gob4","Gob5","Gob6"]
elfNames = ["Elf1","Elf2","Elf3","Elf4","Elf5","Elf6"]
wizNames = ["Wiz1","Wiz2","Wiz3","Wiz4","Wiz5","Wiz6"]
wolfNames = ["Wolf1","Wolf2","Wolf3","Wolf4","Wolf5","Wolf6"]
dragonNames = ["Smaug","The error of the Winds","Nibbler"]
# To draw from names: grab an index using random.randint(0,len(LIST))
# Use the name corresponding to that integer
# delete the item in the list with that index
