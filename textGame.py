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
# Build rooms
#------------

#------------
# Creatures
#------------
gobbly = CM.Goblin("gobbly",10)
#RM.addToRoom('gobbly',10)

#------------
# Game
#------------

pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower(),10)
for x in range(1,26):
	print(x,RM.rooms[x].enemies,RM.rooms[x].items)

VFM.take(Items.startSword.itemName)
VFM.take(Items.startShield.itemName)
print(VFM.equip(Items.startSword.itemName))
print(VFM.equip(Items.startShield.itemName))
startStr = "Armed with their "+Items.startSword.itemName+' '+\
	Items.startSword.itemType+' and '+Items.startShield.itemName+' '+\
	Items.startShield.itemType+', '+pName.capitalize()+\
	' departed into the darkness of the dungeon.'
launch.prettyPrint(gameSpace,startStr)
while True:
	VFM.getInput()
