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
import launch
import Items

#--------------
# Launch screen
#--------------
gameSpace = 60
launch.launchScreen(gameSpace,__doc__)
Items.buildItems()
#------------
# Creatures
#------------
gobbly = CM.Goblin("gobbly")
#------------
# Game
#------------

pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower())
# Generate starting items
startSword = Items.createItem(IM.Sword,"trusty")
startShield = Items.createItem(IM.Shield,'reliable')
VFM.take(startSword.itemName)
VFM.take(startShield.itemName)
print(VFM.equip(startSword.itemName))
print(VFM.equip(startShield.itemName))
startStr = "Armed with their "+startSword.itemName+' '+\
	startSword.itemType+' and '+startShield.itemName+' '+\
	startShield.itemType+', '+pName.capitalize()+\
	' departed into the darkness of the dungeon.'
launch.prettyPrint(gameSpace,startStr)
while True:
	VFM.getInput()
