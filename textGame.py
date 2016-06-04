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
#	Modules Import
#----------------------

import verbFuncMod as VFM
import classMod as CM
import itemMod as IM
import roomMod as RM
import launch
import Items

#--------------
# Launch screen
#--------------
gameSpace = 60
launch.launchScreen(gameSpace,__doc__)
#------------
# Creatures
#------------
gobbly = CM.Goblin("gobbly",RM.startSwp)
#------------
# Game
#------------

VFM.pName = input("\nWhat is your name, brave adventurer: \n")
player = CM.Player('you',RM.startSwp)
VFM.take(Items.startSword.itemName)
VFM.take(Items.startShield.itemName)
print(VFM.equip(Items.startSword.itemName))
print(VFM.equip(Items.startShield.itemName))
startStr = "Armed with their "+Items.startSword.itemName+' '+\
	Items.startSword.itemType+' and '+Items.startShield.itemName+' '+\
	Items.startShield.itemType+', '+VFM.pName.capitalize()+\
	' departed into the darkness of the dungeon.'
launch.prettyPrint(gameSpace,startStr)
while True:
	VFM.getInput()
