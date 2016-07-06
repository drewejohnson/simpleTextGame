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

def say(noun = None,arg2 = None):
	"""Say something"""
	if (noun != None):
		return 'You said "{}"'.format(noun)
	else:
		return 'You said nothing.'


def examine(noun = None,iType = None):
	"""Examine items, enemies, yourself, or the room"""
	# print(noun,iType)
	if (noun != None):
		swp = CM.getLoc()
		if iType == None:
			if noun in RM.rooms[swp].enemies and  noun in CM.GameCharacter.objects:
				return CM.GameCharacter.objects[noun].getDesc()
			elif noun.lower() == 'room':
				return examineRoom()
			elif noun in RM.rooms[swp].items:
				thing = RM.rooms[swp].items[noun]
				# print(thing)
				return thing.getDesc()
			else:
				return "There is no {} here".format(noun)
		else:
			return examineItem(noun,iType)
	else:
		return "Need target to examine."


def examineItem(adj,iType):
	"""Reveal the name and type of item, as well as attributes"""
	item = adj+" "+iType
	onPlayerTpl = CM.GameCharacter.objects['you'].onPerson(item)
	# if item with same adjective is on person,
	# 	onPlayerTpl is (True, item_location)
	#	where item_location displays all items equipped in that spot (arms, pack, etc)
	# else, onPlayerTpl is (False,0)
	if onPlayerTpl[0]:
		if IM.isItem(onPlayerTpl[1][item],iType):
			# check if the item with the noun is of the requested type
			rStr = "{0} {1}\n".format(adj.capitalize(),iType.capitalize())
			rarity = IM.inRare(adj)
			if rarity > 0:
				enhanceStr = IM.allAdj[rarity][adj]
				for c in range(0,len(enhanceStr)):
					if enhanceStr[c] == 'a':
						rStr += "  Attack: +{}\n".format(enhanceStr[c+1])
					elif enhanceStr[c] == 'h':
						rStr += "  Health: +{}\n".format(enhanceStr[c+1])
					elif enhanceStr[c] == 'd':
						rStr += "  Defense: +{}\n".format(enhanceStr[c+1])
			return rStr.rstrip()
		else:
			return "No item {0} {1} equipped nor in pack".\
				format(adj.capitalize(),iType.capitalize())
	else:		# item not on person. Check the room
		swp = CM.getLoc()
		if item in RM.rooms[swp].items:
			if IM.isItem(RM.rooms[swp].items[item],iType):
				rStr = "{0} {1}\n".format(adj.capitalize(),iType.capitalize())
				rarity = IM.inRare(adj)
				if rarity > 0:
					enhanceStr = IM.allAdj[rarity][adj]
					for c in range(0,len(enhanceStr)):
						if enhanceStr[c] == 'a':
							rStr += "  Attack: +{}\n".format(enhanceStr[c+1])
						elif enhanceStr[c] == 'h':
							rStr += "  Health: +{}\n".format(enhanceStr[c+1])
						elif enhanceStr[c] == 'd':
							rStr += "  Defense: +{}\n".format(enhanceStr[c+1])
				return rStr.rstrip()
	return "Item {0} {1} not found on person nor in the room".\
		format(adj.capitalize(),iType.capitalize())



def examineRoom():
	"""Displays the items and enemies in the player's room"""
	thisSwp = CM.getLoc()
	thisRoom = RM.sweepFunc(thisSwp)
	roomStr = "Current room: ({0},{1})\n".format(thisRoom[0],thisRoom[1])
	if len(RM.rooms[thisSwp].enemies) > 0:
		roomStr += 'Enemies: \n'
		for thing in list(RM.rooms[thisSwp].enemies):
			thingType = CM.GameCharacter.objects[thing].className
			if isinstance(RM.rooms[thisSwp].enemies[thing],CM.Player) != True:
				# thingType = CM.GameCharacter.objects[thing].className
				roomStr += '  '+thing.capitalize()#+' the '+thingType+'\n'
			else:
				roomStr += '  '+pName.capitalize()#+' the '+thingType+'\n'
			roomStr +=' the '+thingType+'\n'
	else:
		roomStr += 'Enemies: None\n'
	if len(RM.rooms[thisSwp].items) > 0:
		roomStr += 'Items: \n'
		for item in list(RM.rooms[thisSwp].items):
			iType = RM.rooms[thisSwp].items[item]
			if isinstance(iType,IM.Potion):
				roomStr += "  "+iType.itemType+"\n"
			else:
				roomStr += '  '+item+"\n"
	else:
		roomStr += 'Items: None'
	return roomStr.strip()


def drink(noun = None,arg2 = None):
	"""Drink a healing potion from your inventory"""
	if noun == None:
		#-------CALL A FUNCTION TO SHOW ALL POTIONS
		return "Need a target to drink"
	else:
		if noun == "potion":
			ver = 0
		elif noun == "serum":
			ver  = 1
		elif noun == "elixir":
			ver = 2
		rString =  CM.GameCharacter.objects['you'].drink(ver)
		if rString == 0:
			return "You have no {} to drink".format(noun)
		else:
			return rString


def hit(enemy = None,arg2 = None):
	"""Hit an enemy"""
	if enemy != None:
		swp = CM.getLoc()
		if enemy in RM.rooms[swp].enemies:
			thingObj = RM.rooms[swp].enemies[enemy]
			player = CM.GameCharacter.objects['you']
			status = player.attack(thingObj)
			if status == 1:		# successful attack. enemy strikes back
				print("You struck {0}. {1}'s health: {2}".\
					format(enemy.capitalize(),enemy.capitalize(),thingObj.values[0]))
				status2 = thingObj.attack(player)
				if status2 == 1:
					return "{0} struck back!\nHealth: {1}".\
						format(enemy.capitalize(),player.values[0])
				elif status2 == 2:
					from launch import gameOver
					gameOver(thingObj)
					return ""
				elif status2 == 0:
					return "{0} tried to hit you back and failed.".format(enemy.capitalize())
			elif status == 2:		# killed enemy
				del RM.rooms[swp].enemies[enemy]
				return "You killed {0}!".format(enemy.capitalize())
			elif status == 0:
				return "Attack strength too low. Failed to hit {}".format(enemy)
		else:
			return "There is no {0} in this room".format(enemy)

	else:
		return "Need target to hit"



def take(adj = None,iType = None):
	"""Pick up item and add to inventory"""
	take1 = "You picked up the {}."
	take0 = "There is no {} here."
	if(adj != None):
		pLoc = CM.getLoc()
		if len(RM.rooms[pLoc].enemies) >1: # player is not alone in the room
			return "Enemies block your way! Defeat them to grab the loot!"
		if iType != None:
			item = adj+" "+iType
			if item in RM.rooms[pLoc].items:
				thing = RM.rooms[pLoc].items[item] # object instance of item
				if IM.isItem(thing,iType):
		# True if there is an item of the type iType with the
		# specified adjective in the room
					del RM.rooms[pLoc].items[item]
					CM.GameCharacter.objects['you'].pack[item]=thing
					return take1.format(item)
				else:
					return take0.format(item)
			else:
				return take0.format(item)
		else:		# no value of iType given
			if adj in RM.rooms[pLoc].items: # check if item is a potion
				thing = RM.rooms[pLoc].items[adj]
				if isinstance(thing,IM.Potion):
					CM.Player.potions[thing.var] += 1
					del RM.rooms[pLoc].items[adj]
					return take1.format(thing.itemType)
			else:
				return take0.format(adj)
	else:
		return "Need target to take"


def getInput():
	command = input(": ").split()
	verbIn = command[0].lower()
	if verbIn in verbDict:
		verb = verbDict[verbIn]
	else:
		print("Unknown verb {}".format(verbIn))
		return 0
	if verbIn.lower() == 'quit':
		return quitGame()
	else:
		try:
			arg1 = command[1].lower()
			if arg1 == 'self' or arg1 == pName:
				arg1 = 'you'
		except IndexError:
			arg1 = None
		try:
			arg2 = command[2].lower()
		except IndexError:
			arg2 = None
		print(verb(arg1,arg2))
		return None


def help(vHelp = None,arg2 = None):
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


def equip(adj = None,iType = None):
	"""Equip an object from your pack"""
	equipStr = "You equiped the "
	if(adj == None):
		return 'Need target to equip'
	else:
		if iType != None:
			equipObj = adj+" "+iType
			if equipObj in CM.Player.pack:
				thing = CM.Player.pack[equipObj]
				eStr = IM.allAdj[IM.inRare(adj)][adj]
				# string to enhance attribute
				if (thing.equipSlot[0] == 'a'):
					if (len(CM.Player.arms)<=2):
						CM.Player.arms[equipObj] = thing
						del(CM.Player.pack[equipObj])
						CM.GameCharacter.objects['you'].valEnhance(eStr,0)
						return equipStr+"{0} {1}".\
							format(thing.itemName,thing.itemType)
					else:
						return equipFull('arms')
				elif(thing.equipSlot[0] == 'l'):
					if(len(CM.Player.legs)<=2):
						CM.Player.legs[equipObj] = thing
						CM.GameCharacter.objects['you'].valEnhance(eStr,0)
						del(CM.Player.pack[equipObj])
						return equipStr+"{0} {1}".\
							format(thing.itemName,thing.itemType)
					else:
						return equipFull('legs')
				elif(thing.equipSlot[0] == 'h'):
					if(len(CM.Player.head)<=1):
						CM.Player.head[equipObj] = thing
						CM.GameCharacter.objects['you'].valEnhance(eStr,0)
						del(CM.Player.pack[equipObj])
						return equipStr+"{0} {1}".\
							format(thing.itemName,thing.itemType)
					else:
						return equipFull('head')
			else:
				return "No item {} in pack.".format(equipObj)
		else:
			return "EQUIP - Will add a routine to show all items in pack with a given adjective"


def equipFull(equipSlot):
	"""Error message for equipping an item to a full slot"""
	return "{} full. Need to drop an item.".format(equipSlot.capitalize())


def unequip(adj = None,iType = None):
	"""Unequip an item and place it in your pack"""
	if adj != None:
		eStr = IM.allAdj[IM.inRare(adj)][adj]
		if iType != None:
			item = adj+" "+iType
			if item in CM.Player.arms:
				itemCls = CM.Player.arms[item]
				del CM.Player.arms[item]
				# eStr = IM.allAdj[IM.inRare(item)][item]
				CM.GameCharacter.objects['you'].valEnhance(eStr,1)
				CM.Player.pack[item] = itemCls
				return "You unequipped the {}.".format(item)
			elif item in CM.Player.legs:
				itemCls = CM.Player.legs[item]
				del CM.Player.legs[item]
				CM.GameCharacter.objects['you'].valEnhance(eStr,1)
				CM.Player.pack[item] = itemCls
				return "You unequipped the {}".format(item)
			elif item in CM.Player.head:
				itemCls = CM.Player.head[item]
				del CM.Player.head[item]
				CM.GameCharacter.objects['you'].valEnhance(eStr,1)
				CM.Player.pack[item] = itemCls
				return "You unequipped the {}".format(item)
			else:
				return "Item {} not equipped.".format(item)
		else:
			print("UNEQUIP - Will add a routine to show all items in pack with a given adjective")
	else:
		return "Need target to unequip."


def move(direction = None,arg2 = None):
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
			toSwp = nbors[d]
			toPos = RM.sweepFunc(toSwp)
			# RM.addToRoom('you',toSwp)
			# RM.delFromRoom('you',curSwp)
			RM.rooms[toSwp].enemies['you'] = CM.GameCharacter.objects['you']
			del RM.rooms[curSwp].enemies['you']
			del CM.Player.pos[curSwp]
			CM.Player.pos[toSwp] = RM.rooms[toSwp]
			return 'Moved from {0} to {1}'.format(curPos,toPos)
		else:
			return 'No door in that direction.'
	else:
		return "{} is not a valid direction of movement.".format(direction.capitalize())


def validCoord(curcoord,dim):
	"""Returns true if curcoord within gamespace dimension dim"""
	# dim == 0 => x, dim == 1 => y
	if curcoord > 0:
		if dim == 0: # moving in x
			if curcoord <= RM.roomsX:
				return True
			else:
				return False
		elif dim == 1: # moving in y
			if curcoord <= RM.roomsY:
				return True
			else:
				return False
		else:
			raise SystemExit('Bad Dimension in validCoord')
	else:
		return False


def quitGame(val = None,arg2 = None):
	"""Quit the game"""
	print('You are about to quit the game. If you do so, you will lose'+\
		' all progress.\nAre you sure you want to do this?\n')
	quitVal = str(input('Press y to quit\n: ')).lower()
	if quitVal == 'y':
		# print('Until next time, brave adventurer.')
		raise SystemExit('Until next time, brave adventurer.')
	else:
		print('Carry on!')
		return 0


# Verb Dictionary
verbDict = {
	"say": say,
	"examine": examine,
	"hit": hit,
	"help": help,
	"take": take,
	"equip": equip,
	"move": move,
	"quit": quitGame,
	"unequip": unequip,
	"drink":drink,
	# "strike":strike,
}
sortedVerbs = sorted(verbDict)

pName = ""
