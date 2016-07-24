#-------------------
# Andrew Johnson
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze,
fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import/ Game Preparation
#----------------------

import launch
import roomMod as RM
import itemMod as IM
import verbFuncMod as VFM
import tutorial



launch.launchScreen()
print(VFM.help())
RM.buildGame()


dummy = input("Enter 'y' to begin a tutorial.\n: ")
if len(dummy) > 0 and dummy[0].lower() == 'y':
	tutorial.teachGame()

startStr = "Armed with their "+IM.startSword.itemName+' '+\
	IM.startSword.itemType+' and '+IM.startShield.itemName+' '+\
	IM.startShield.itemType+', '+VFM.player.name.capitalize()+\
	' departed into the darkness of the dungeon.'

launch.prettyPrint(startStr)
while True:
	VFM.getInput()
