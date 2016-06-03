#-------------
# Andrew Johnson
#
# Simple Text based Game
#-------------

"""Module for various verb functions"""
#----------------------
#	Modules Import
#----------------------
import classMod as CM
import itemMod as IM
import roomMod as RM
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
		elif noun.lower() == 'room':
			return examineRoom()
		else:
			return "There is no {} here".format(noun)
	else:
		return "Need target to examine."


def examineRoom():
	"""Displays the items and enemies in the player's room"""
	thisRoom = CM.getLoc()
	roomStr = ""
	if len(RM.rooms[thisRoom].enemies) > 1:
		roomStr = 'Enemies: \n'
		for thing in list(RM.rooms[thisRoom].enemies):
			if isinstance(RM.rooms[thisRoom].enemies[thing],CM.Player) != True:
				thingType = CM.GameCharacter.objects[thing].className
				roomStr += '  '+thing.capitalize()+' the '+thingType+'\n'
	else:
		roomStr = 'Enemies: None\n'
	if len(RM.rooms[thisRoom].items) > 0:
		roomStr += 'Items: \n'
		for item in list(RM.rooms[thisRoom].items):
			iType = RM.rooms[thisRoom].items[item].itemType
			roomStr += '  '+item+' '+iType+'\n'
	else:
		roomStr += 'Items: None'
	return roomStr.strip()




def hit(noun = None):
	"""Hit an enemy"""
	if (noun != None):
		if noun in CM.GameCharacter.objects:
# there is a noun to hit
			thing = CM.GameCharacter.objects[noun]
# thing is the class of noun
			thing.health = thing.health -1
			if thing.health <= 0:
				return "You killed {}!".format(thing.name)
			else:
				return "You hit {}".format(thing.name)
		else:
			return "There is no {} here.".format(noun)
	else:
		return 'Need target to hit'


def take(takeItem = None):
	"""Pick up item and add to inventory"""
	if(takeItem != None):
		if takeItem in IM.RoomItem.objects:
			pLoc = CM.getLoc()
			if takeItem in RM.rooms[pLoc].items:
				thing = IM.RoomItem.objects[takeItem]
				if RM.delFromRoom(takeItem,pLoc) == 0:
					CM.Player.pack[takeItem] = thing
					return "You picked up the {0} {1}".format(takeItem,\
					thing.itemType)
				else:
					return 'Could not delete item from room'
			else:
				return "There is no {} here".format(takeItem)
		else:
			return 'No item by that name.'
	else:
		return "Need target to take"


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
		if nounIn == pName or nounIn.lower() == 'self':
			nounIn = 'you'
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


def move(direction = None):
	"""Select a compass direction (NSEW) to move the player"""
	curSwp = CM.getLoc()
	curPos = RM.sweepFunc(curSwp)
	nbors = {}	# keys: valid directions; values: corresponding room
	# North
	if validCoord(curPos[1]+1,1):
		nbors['north'] = RM.sweepFunc(curPos[0],curPos[1]+1)
	if validCoord(curPos[1]-1,1):
		nbors['south'] = RM.sweepFunc(curPos[0],curPos[1]-1)
	if validCoord(curPos[0]-1,0):
		nbors['west'] = RM.sweepFunc(curPos[0]-1,curPos[1])
	if validCoord(curPos[0]+1,0):
		nbors['east'] = RM.sweepFunc(curPos[0]+1,curPos[1])
	if direction == None:
		mvStr = 'Possible directions:\n'
		if 'north' in nbors:
			mvStr += 'North\n'
		if 'east' in nbors:
			mvStr += 'East\n'
		if 'south' in nbors:
			mvStr += 'South\n'
		if 'west' in nbors:
			mvStr += 'West'
			return mvStr
		else:
			return mvStr.strip()
	elif direction.lower() in ['north','south','east','west']:
		d = direction.lower()
		if d in nbors:
			toSwp = RM.sweepFunc(nbors[d])
			print(toSwp)
			RM.addToRoom(CM.Player,toSwp)
			RM.delFromRoom('you',curSwp)
			return 'Moved from {0} to {1}'.format(curPos,toSwp)
		else:
			return 'No door in that direction.'
	else:
		return "{} is not a valid direction of movement.".format(direction.capitalize())

def validCoord(curcoord,dim):
	"""Returns true if curcoord within gamespace dimension dim"""
	# dim == 0 => x, dim == 1 => y
	if curcoord > 0:
		if dim == 0: # moving in x
			if curcoord < RM.roomsX:
				return True
			else:
				return False
		elif dim == 1: # moving in y
			if curcoord < RM.roomsY:
				return True
			else:
				return False
		else:
			raise SystemExit('Bad Dimension in validCoord')
	else:
		return False

# Verb Dictionary
verbDict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"help": help,
	"take": take,
	"equip": equip,
	"move": move,
}
sortedVerbs = sorted(verbDict)

pName = ""
