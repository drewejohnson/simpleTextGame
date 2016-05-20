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

def say(noun):
	return 'You said "{}"'.format(noun)

def examine(noun):
	if noun in CM.GameObject.objects:
		return CM.GameObject.objects[noun].getDesc()
	else:
		return "There is no {} here".format(noun)
# looks for an object wth name noun in GameObjects object		
def hit(noun):
	if noun in CM.GameObject.objects:
		thing = CM.GameObject.objects[noun]
		thing.health = thing.health -1
		if thing.health <= 0:
			msg = "You killed the {}!".format(thing.className)
		else:
			msg = "You hit the {}".format(thing.className)
	else:
		msg = "There is no {} here.".format(noun)
	return msg