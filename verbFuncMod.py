#-------------
# Andrew Johnson
#
# Simple Text based Game
#-------------

"""
Module for various verb functions
"""
#----------------------
#	Modules Import
#----------------------
import classMod as CM
import itemMod as IM
#----------------------
#	Verb Functions
#----------------------

def say(noun = None):
	"""Say something"""
	if (noun != None):
		return 'You said "{}"'.format(noun)
	else:
		return 'You said nothing.'

def examine(noun = None):
	"""Examine an object, enemy, or player"""
	if (noun != None):
		if noun in CM.GameCharacter.objects:
			return CM.GameCharacter.objects[noun].getDesc()
		else:
			return "There is no {} here".format(noun)
	else:
		return "Need target to examine."
# looks for an object wth name noun in GameCharacter
def hit(noun = None):
	"""Hit an enemy"""
	if (noun != None):
		if noun in CM.GameCharacter.objects:
# there is a noun to hit
			thing = CM.GameCharacter.objects[noun]
# thing is the class of noun
			thing.health = thing.health -1
			if thing.health <= 0:
				msg = "You killed {}!".format(thing.name)
			else:
				msg = "You hit {}".format(thing.name)
		else:
			msg = "There is no {} here.".format(noun)
	else:
		msg = 'Need target to hit'
	return msg

def take(takeItem = None):
	"""Pick up item and add to inventory"""
	if(takeItem != None):
		if takeItem in IM.RoomItem.objects:
			thing = IM.RoomItem.objects[takeItem]
			CM.Player.pack[takeItem] = thing
			takeMsg = "You picked up the {0} {1}".format(takeItem,\
				thing.itemType)
		else:
			takeMsg = "There is no {} here".format(takeItem)
	else:
		takeMsg = "Need target to take"
	return takeMsg

def getInput():
	command = input(": ").split()
	verbIn = command[0].lower()
	if verbIn in verbDict:
		verb = verbDict[verbIn]
	else:
		print("Unknown verb {}".format(verbIn))
		return
	if len(command)>=2:
		nounIn = command[1].lower()
		print(verb(nounIn))
	else:
		print(verb())

def help(vHelp = None):
	"""Return descriptions on various actions"""
	helpMsg = " "
	helpStr = "{0:10s} -{1:20s}\n"
	if(vHelp != None):
		if(vHelp in verbDict):
			helpMsg = helpStr.format(vHelp,verbDict[vHelp].__doc__)
		else:
		# verb not found in dictionary, return verbs with same first letter
			helpMsg = 'No specific action "{}"'.format(vHelp)+'\n'
			for key in sortedVerbs:
				if(vHelp[0]==key[0]):
					helpMsg += helpStr.format(key,verbDict[key].__doc__)
	else:
		for key in sortedVerbs:
			helpMsg += helpStr.format(key,verbDict[key].__doc__)
	return helpMsg.strip()

def equip(equipObj = None):
	"""Equip an object from your pack"""
	equipStr = "You equiped the "
	if(equipObj == None):
		return 'Need target to equip'
	else:
		if equipObj in CM.Player.pack:
			thing = CM.Player.pack[equipObj]
			if (thing.equipSlot[0] == 'a'):
				if (len(CM.Player.arms)<=2):
					CM.Player.arms[equipObj] = thing
					del(CM.Player.pack[equipObj])
					return equipStr+"{0} {1}".\
						format(thing.itemName,thing.itemType)
				else:
					return equipFull('arms')
			elif(thing.equipSlot[0] == 'l'):
				if(len(CM.Player.legs)<=2):
					CM.Player.legs[equipObj] = thing
					del(CM.Player.pack[equipObj])
					return equipStr+"{0} {1}".\
						format(thing.itemName,thing.itemType)
				else:
					return equipFull('legs')
			elif(thing.equipSlot[0] == 'h'):
				if(len(CM.Player.head)<=1):
					CM.Player.head[equipObj] = thing
					del(CM.Player.pack[equipObj])
					return equipStr+"{0} {1}".\
						format(thing.itemName,thing.itemType)
				else:
					return equipFull('head')
		else:
			return "No item {} in pack.".format(equipObj)

def equipFull(equipSlot):
	"""Error message for equipping an item to a full slot"""
	return "{} full. Need to drop an item.".format(equipSlot.capitalize())

# Verb Dictionary
verbDict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"help": help,
	"take": take,
	"equip": equip,
}
sortedVerbs = sorted(verbDict)
