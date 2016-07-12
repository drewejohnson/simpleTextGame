#-----------
# Andrew Johnson
#
# Simple Text based Game
#-----------
"""Creation of various game objects and creatures"""
#------------
# Imports
#------------
import random as R
import roomMod as RM
import verbFuncMod as VFM
import itemMod as IM
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
		GameCharacter.objects[self.name.lower()] = self
		self.values = values
		RM.rooms[sweep].enemies[self.name.lower()] = self
		# print("Added a {0} {1} to room {2}".format(name,self,RM.sweepFunc(sweep)))
		# self.name stores keys as character names, not classNames



	def getDesc(self):
		return self.desc


	@property
	def desc(self):
		return self._desc+"\nHealth: {0:3d} Attack: {1:3d} Defense: {2:3d}"\
			.format(self.values[0],self.values[1],self.values[2])


	@desc.setter
	def desc(self,value):
		self._desc = value


	def enhance(self,eStr):
		"""Way to increase the enemy difficulty using a given adjective"""
		if eStr != None:
			if len(eStr)%2 != 0:
				raise SystemExit('Odd string length for enemyEnhance {0} on {1}'.\
					format(eStr,self))
			else:
				for c in range(0,len(eStr),2):
					if eStr[c] == 'a':
						self.values[1] += int(eStr[c+1])
					elif eStr[c] == 'd':
						self.values[2] += int(eStr[c+1])
					elif eStr[c] == 'h':
						self.values[0] += int(eStr[c+1])
					else:
						raise SystemExit("Bad enhancer {} in enemyEnhance".format(eStr))
			# print("Applied enhancement {0} to {1}".format(eStr,self))


	def attack(self,other):
		"""Character self attacks other"""
		if self.values[1] == 0:
			return 0
		combatDiff = self.values[1] - other.values[2]
		if combatDiff > 0:
			if combatDiff >= other.values[0]:
				other.values[0] = 0
				return 2		# other is dead
			else:
				other.values[0] -= combatDiff
			return 1		# successful attack
		else:
			if R.random() > 0.5:		# random chance to attack anyways
				if combatDiff >= other.values[0]:
					other.values[0] = 0
					return 2
				else:
					other.values[0] -= abs(combatDiff)*int(R.random())
					return 1
			else:
				return 0		# failed attack

class Goblin(GameCharacter):
	def __init__(self,name,sweep,adj = None):#,locX,locY):
		self.className = "goblin"
		gobValues = [5,5,5]			# 5 health, 1 attack and defense
		super().__init__(name,sweep,gobValues)#,locX,locY)
		self._desc = "A foul goblin called "+self.name.capitalize()
		if adj != None:
			self._desc += " the {}".format(adj.capitalize())
			# super().enhance(adj)


class Werewolf(GameCharacter):
	def __init__(self,name,sweep,adj = None):
		self.className = "werewolf"
		wolfValues = [6,7,6]
		super().__init__(name,sweep,wolfValues)
		self._desc = "A ferocious wolf named "+self.name.capitalize()
		if adj != None:
			self._desc += " the {}".format(adj.capitalize())
			# super().enemyEnhance(adj)


class Elf(GameCharacter):
	def __init__(self,name,sweep,adj=None):
		self.className = "elf"
		elfValues = [7,7,7]
		super().__init__(name,sweep,elfValues)
		self._desc = "An estranged elf named {}".format(self.name.capitalize())
		if adj != None:
			self._desc += " the {}".format(adj.capitalize())
			# super().enemyEnhance(adj)


class Wizard(GameCharacter):
	def __init__(self,name,sweep,adj=None):
		self.className = "wizard"
		wizValues = [9,6,7]
		super().__init__(name,sweep,wizValues)
		self._desc = "A powerful wizard named {}".format(self.name.capitalize())
		if adj != None:
			self._desc += " the {}".format(adj.capitalize())
			# super().enemyEnhance(adj)


class Dragon(GameCharacter):
	def __init__(self,name,sweep,adj=None):
		self.className = "dragon"
		dragonValues = [15,15,15]
		super().__init__(name,sweep,dragonValues)
		self._desc = "An enraged, gigantic dragon known as {}".format(self.name.capitalize())
		if adj != None:
			self._desc += " the {}".format(adj.capitalize())
			# super().enemyEnhance(adj)


class Player(GameCharacter):
	# arms = {}
	# legs = {}
	# head = {}
	# pack = {}
	# pos = {}
	potions = [0,0,0]

	def __init__(self,name,sweep):#,locX,locY):
		self.className = "Adventurer"
		self.values = [7,5,5]
		self.maxHealth = self.values[0]
		# self.potions = [0,0,0]
		super().__init__(name.lower(),sweep,self.values)#,locX,locY)
		# self.pos[sweep] = RM.rooms[sweep]
		self.sweep = sweep		# player location
		self.prevSwp = sweep
		self.arms = {}
		self.legs = {}
		self.head = {}
		self.pack = {}
		self._desc = "A brave adventurer named "+VFM.pName.capitalize()


	@property
	def desc(self):
		"""Returns a string with the inventory and location of the player"""
# Maybe put the parsing through dictionaries into a class method at some point
		stats = "Health: {0:3d}/{1:<3d} Attack: {2:3d} Defense: {3:3d}\n".\
			format(self.values[0],self.maxHealth,self.values[1],self.values[2])
		location = "Location: ({0},{1})\n".\
			format(RM.sweepFunc(self.sweep)[0],RM.sweepFunc(self.sweep)[1])
			# format(RM.sweepFunc(getLoc())[0],RM.sweepFunc(getLoc())[1])
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
			# pString = [0,0,0]
			for item in self.pack:
				if not isinstance(self.pack[item],IM.Potion):
					inventory += "  {0} {1}\n".format(self.pack[item].itemName,\
						self.pack[item].itemType)
		if self.potions[0] > 0:
			inventory += "Potions: {0}  +{1} health\n".\
				format(self.potions[0],IM.Potion.values[0])
		if self.potions[1] > 0:
			inventory += "Serums: {0}  +{1} health\n".\
				format(self.potions[1],IM.Potion.values[1])
		if self.potions[2] > 0:
			inventory += "Elixirs: {0}  +{1} health\n".\
				format(self.potions[2],IM.Potion.values[2])
		return self._desc+"\n"+stats+location+inventory.rstrip()


	def onPerson(self,noun):
	    """Return the location of an equipped item with name noun"""
	    if noun in self.arms:
	        return (True,self.arms)
	    elif noun in self.legs:
	        return (True,self.legs)
	    elif noun in self.head:
	        return (True,self.head)
	    elif noun in self.pack:
	        return (True,self.pack)
	    else:
	        return (False,0)

	@desc.setter
	def desc(self,value):
		self._desc = value


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
				self.maxHealth += int(enhanceStr[c+1])*(-1)**eMod
				return 0
			else:
				raise SystemExit("Bad enhancer in valEnhance")


	def drink(self,ver):
		if self.values[0] == self.maxHealth:
			return "Already at full health. No need to heal"
		if self.potions[ver] > 0:
			self.potions[ver] -= 1
			if self.values[0] + IM.Potion.values[ver] > self.maxHealth:
				self.values[0] = self.maxHealth
			else:
				self.values[0] += IM.Potion.values[ver]
			return "You drank the {0}. Current health: {1}/{2:<}".\
				format(IM.Potion.types[ver],self.values[0],self.maxHealth)
		else:
			return 0

#-----------
# Enemy Names
#------------

gobNames = ["Gnarly","Dopy","Greasy","Jabber","Grimy"]
elfNames = ["Legalad","Legolike","Legalass","Legless"]
wizNames = ["Merlin","Grandalf","Dumbledude","Snep","Moldewart","Whiny"]
wolfNames = ["CrookedTeeth","ThickFur","Str8killah","Howler","-undecipherable-"]
dragonNames = ["Smaug","Toothless","Nibbler"]
# To draw from names: grab an index using random.randint(0,len(LIST))
# Use the name corresponding to that integer
# delete the item in the list with that index
