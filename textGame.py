#-------------------
# Andrew Johnson
# 19 May, 2016
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze, fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import
#----------------------

import verbFuncMod as VFM
import classMod as CM

#-----------
# Functions for handing user commands
#-----------	
def getInput():
	command = input(": ").split()
	verbIn = command[0]
	if verbIn in verbDict:
		verb = verbDict[verbIn]
	else:
		print("Unknown verb {}".format(verbIn))
		return
	if len(command)>=2:
		nounIn = command[1]
		print(verb(nounIn))
	else:
		print(verb())
		
verbDict = {
	"say": VFM.say,
	"examine": VFM.examine,
	"hit": VFM.hit,
	"help":VFM.help,
}

#------------
# Creatures
#------------
goblin = CM.Goblin("Gobbly")
#------------
# Game
#------------
pName = input("What is your name, brave adventurer: \n")
player = CM.Adventurer(pName)
print("And so, "+pName+' departed on their brave quest into the unknown!')
while True:
	getInput()