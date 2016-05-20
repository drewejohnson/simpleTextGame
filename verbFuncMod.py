#-------------
# Andrew Johnson
# 19 May, 2016
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

#----------------------
#	Verb Functions
#----------------------

def say(noun = None):
	"""Say something"""
	if (noun != None):
		return 'You said "{}"'.format(noun)
	else:
		return 'You said nothing.'

def examine(noun = 'nothing'):
	"""Examine an object or enemy"""
	if (noun != None):
		if noun in CM.GameObject.objects:
			return CM.GameObject.objects[noun].getDesc()
		else:
			return "There is no {} here".format(noun)
	else:
		return "Need target to examine."
# looks for an object wth name noun in GameObjects object		
def hit(noun = None):
	"""Hit an enemy"""
	if (noun != None):
		if noun in CM.GameObject.objects:
			thing = CM.GameObject.objects[noun]
			thing.health = thing.health -1
			if thing.health <= 0:
				msg = "You killed the {}!".format(thing.className)
			else:
				msg = "You hit the {}".format(thing.className)
		else:
			msg = "There is no {} here.".format(noun)
	else:
		msg = 'Need target to hit'
	return msg

def help(vHelp = None):
	"""Give help on specific actions"""
	vList = ['say','help','examine']
	if(vHelp != None):
		if(vHelp[0] == 's'):
			return "{0:10s}{1:20s}".format('say',say.__doc__)
		elif(vHelp[0] == 'h'):
			return "{0:10s}{1:20s}".format('hit',hit.__doc__)
		elif(vHelp[0] == 'e'):
			return "{0:10s}{1:20s}".format('examine',examine.__doc__)
	else:
		return 'Arbitrary help to come later'